$(function () {

    loadDirectionType();
    DataInSticks();
});

//var evaluationDataUrl = 'datas.json';
var evaluationDataUrl = '/api/evaluation/data';

var nSixMonth = GetNearMonth().reverse(); //建立近6个月的数组
var pRateArry = QureyWinRate(1);
var eRateArry = QureyWinRate(2);

function loadDirectionType() {
    myGet(evaluationDataUrl, function(data){
    	//多空单总计
        var plus_trade = 0;
        var empty_trade = 0;        
        //多空单盈亏次数
        var plus_wins = 0;
        var empty_wins = 0;
        var plus_lose = 0;
        var empty_lose = 0;
        var tradeCount = 0;
        //盈亏额
        var pProfit = 0;
        var eProfit = 0;
        var pDmg = 0;
        var eDmg = 0;
        //成交量
        var pCount = 0;
        var eCount = 0;
        //手续费合计
        var pTotalCommission = 0;
        var eTotalCommission = 0;
        $(data).each(function(k, v) {
            if (v.direction_type == 1){
            	plus_trade += 1;
            	tradeCount += 1;
            	pCount += v.volume;
            	pTotalCommission += v.commission;
            	if (v.profit > 0){
            		plus_wins += 1;
            		pProfit += v.profit
            	}
            	else{
            		pDmg += v.profit
            	}
            	
            }
            else if (v.direction_type == 2){
            	empty_trade += 1;
            	tradeCount += 1;
            	eCount += v.volume;
            	eTotalCommission += v.commission;
            	if (v.profit > 0){
            		empty_wins += 1
            		eProfit += v.profit
            	}
            	else{
            		eDmg += v.profit
            	}
            }
            
        });
        //盈亏次数计算
        plus_lose = plus_trade - plus_wins;
        empty_lose = empty_trade -empty_wins;
        var winTradeCount = plus_wins + empty_wins;
        var loseTradeCount = tradeCount - winTradeCount;
        //多空胜率计算
        var perPlusWin = (plus_wins / plus_trade)*100;
        var perEmptyWin = (empty_wins / empty_trade)*100;
        perPlusWin = perPlusWin.toFixed(2);
        perEmptyWin = perEmptyWin.toFixed(2);
        //盈亏比计算
        var pRateSum = CountRateSum(pProfit,plus_wins,pDmg,plus_lose,pTotalCommission);
        var eRateSum = CountRateSum(eProfit,empty_wins,eDmg,empty_lose,eTotalCommission);
        
        //写入数据到页面
        $('#pWinRate').text(perPlusWin + "%");
        $('#eWinRate').text(perEmptyWin + "%");
        $('#pTrade').text(plus_trade);
        $('#eTrade').text(empty_trade);
        $('#pCounts').text(pCount);
        $('#eCounts').text(eCount);
//      $('#pRateSums').text(pRateSum + "%");
//      $('#eRateSums').text(eRateSum + "%");
        
//      console.log(eTotalCommission);
        
        //写入统计数据到图形
        DataInPie(plus_trade,empty_trade);
        
        
    });
}

//盈亏比算法公式
function CountRateSum(winSum,winTradeCount,loseSum,loseTradeCount,totalCommission){
	//总体盈亏比= （总体盈利额/总盈利次数）/（总体亏损额/ 总亏损次数+总体手续费/(总盈利次数+总亏损次数)））x 100%
	var rateSum = (winSum / winTradeCount)/(loseSum/loseTradeCount + totalCommission/(winTradeCount+loseTradeCount))*100;
	rateSum = rateSum.toFixed(2);
	return rateSum
}

//盈亏比算法公式
//function CountRateSum(winSum,winTradeCount,loseSum,loseTradeCount,totalCommission){
//	//总体盈亏比= （总体盈利额/总盈利次数）/（总体亏损额/ 总亏损次数+总体手续费/(总盈利次数+总亏损次数)））x 100%
//	var rateSum = (winSum / winTradeCount)/(loseSum/loseTradeCount + totalCommission/(winTradeCount+loseTradeCount))*100;
//	rateSum = rateSum.toFixed(2);
//	return rateSum
//}

//柱状数据筛选
function QureyWinRate(x) {
	var pRateArry = new Array();
    var pWinm = 0;
	var pTotalm = 0;	   
	var pRatem = 0;
    myGet(evaluationDataUrl, function(data){    	
    	for (i=0;i<5;i++){   
    		pWinm = 0;
	        pTotalm = 0;
    		$(data).each(function(k, v) {
	        	//多单计算	        	
	            if (nSixMonth[i] == v.trade_date.substring(0,7) && v.direction_type == x){            	
	            	pTotalm +=1;
	            	if (v.profit > 0){
	            		pWinm += 1
	            	}
	            }            	            
	        }); 
	        pRatem = (pWinm/pTotalm)*100;
	        pRateArry[i] = pRatem.toFixed(2);
    	}        
        console.log(pRateArry);        
    });    
    return pRateArry
}



//获取近6个月的时间
function GetNearMonth(){
//创建现在的时间
	var data=new Date();
	//获取年
	var year=data.getFullYear();
	//获取月
	var mon=data.getMonth()+2;
	var arry=new Array();
	for(var i=0;i<5;i++){
		mon=mon-1;
		if(mon<=0){
			year=year-1;
			mon=mon+12;
		}
		if(mon<10){
			mon="0"+mon;
		}					
		arry[i]=year+"-"+mon;
	}				
	console.log(arry);
	return arry;
}

//日期格式化
function Appendzero(obj){
	if(obj<10) return "0" +""+ obj;
	else return obj;
}


//多空分布图形数据
function DataInPie(plus_trade,empty_trade){
	var dom = document.getElementById("dkdPie");
			var myChart = echarts.init(dom);
			var app = {};
			option = null;
			option = {
				
//			    title : {
//			        text: '',
//			        subtext: '多空单分布',
//			        x:'center'
//			    },
			    tooltip : {
			        trigger: 'item',
			        position: ['30%', '70%'],
			        formatter: "{a} <br/>{b} : {c} ({d}%)"
			    },

				color:['#4b85fb','#d93770'],
			    series : [
			        {
			            name: 'direction_type',
			            type: 'pie',
			            radius : '65%',
			            center: ['50%', '50%'],
			            data:[
			                {value:plus_trade, name:'多单'},
			                {value:empty_trade, name:'空单'}
			            ],
			            label:{
			            	color:'#ffffff'
			            },
			            itemStyle: {
			            	
			                emphasis: {
			                    shadowBlur: 10,
			                    shadowOffsetX: 0,
			                    shadowColor: 'rgba(255, 0, 0, 0.5)'
			                }
			            }
			        }
			    ]
			};
			
			if (option && typeof option === "object") {
			    myChart.setOption(option, true);
			}
}

//胜率柱状图
function DataInSticks(){
	
	var dom1 = document.getElementById("winRateSticks");
	var myChart1 = echarts.init(dom1);
	var app1 = {};
	option = null;
	
	
	option = {
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {
	            type: 'cross',
	            crossStyle: {
	                color: '#999'
	            }
	        }
	    },	   
	    legend: {
	        data:[
	        		{
	        			name:'多单',
	        			textStyle:{color:'#fff'}	        	
	        		},
	        		{
	        			name:'空单',
	        			textStyle:{color:'#fff'}	        	
	        		}
	        	]
	    },
	    xAxis: [
	        {
	            type: 'category',
	            data: nSixMonth,
	            axisPointer: {
	                type: 'shadow'
	            },
	            axisLine:{
			        lineStyle:{
			            color:'#999',
			            width:1
			        }
			    }
	        }
	    ],
	    yAxis: [
	        {
	            type: 'value',
	            splitLine:{
	            	show: true,
	            	lineStyle:{
	            		color:'#666'
	            		}
	            },
	            name: '胜率(%)',
	            min: 0,
	            max: 100,
	            interval: 20,
	            axisLine:{
			        lineStyle:{
			            color:'#999',
			            width:1
			        }
			    }
	        }
	    ],
	    color:['#4b85fb','#d93770'],
	    
	    series: [	    
	        {	        	
	            name:'多单',
	            type:'bar',
//	            barWidth:5,
	            data:pRateArry
	        },
	        {
	            name:'空单',
	            type:'bar',
	            data:eRateArry
	        }
	    ]
	};
	if (option && typeof option === "object") {
	    myChart1.setOption(option, true);
	}
}

$(function () {
    // bindRange('evaluationScore');
    bindSubmit();
    loadDataList();
});
var evaluationRef = {10: '1分钟', 50: '5分钟', 150: '15分钟'};
var directionTypeRef = {1: '多单', 2: '空单'}

var evaluationDataUrl = '/api/evaluation/data'
function bindSubmit() {
    $('#dataForm').submit(function(){
        return false;
    })
    $('input[type="submit"]').click(function(){
    	$('input[type="submit"]').attr("disabled","disabled");
    	$('input[type="submit"]').val("保存中");
        myPost(evaluationDataUrl, objectifyForm('dataForm'), function(data){
            // console.log(data)
            toasts('saveData');
            loadDataList();
            fromClear('dataForm');
            $('input[type="submit"]').removeAttr("disabled");
    		$('input[type="submit"]').val("保存");
        });        
    });
}

function removeData(id) {
    myDelete(evaluationDataUrl, {id: id}, function(){
        loadDataList()
    })
}

function loadDataList() {
    myGet(evaluationDataUrl, function(data){
        $('#dataList').find('.dataNode').remove();
        var h = '';
        $(data).each(function(k, v) {
            h += '<tr class="dataNode">';
            h += '<td>'+v.trade_date+'</td>';
            // h += '<td>'+v.position_time_str+'</td>';
            var profitClass = v.profit > 0 ? 'win' : 'lose'
            h += '<td><span class="'+(profitClass)+'">'+v.profit+'</span></td>';
            h += '<td>'+v.commission+'</td>';
            h += '<td>'+v.volume+'</td>';
            h += '<td>'+directionTypeRef[v.direction_type]+'</td>';
            h += '<td>'+v.trading_variety+'</td>';
            h += '<td><a href="javascript:removeData('+v.id+')" >删除</a></td>';
            h += '</tr>';
        });
        $('#dataList').append(h);
    });
}

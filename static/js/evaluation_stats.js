$(function(){
    loadGeneral();
    loadUnit();
});

function loadGeneral() {
    myGet('/api/evaluation/stats/general', function(data){

        $.each(data, function(k, v){

            if (k.indexOf('sum') > 0) {
                v = myRound(v, 3)
            }
            if (k.indexOf('rate') > 0) {
                v = myRound(v, 2)
            }
            if (k.indexOf('count') > 0) {
                v = myRound(v, 0)
            }
            $('#'+ k).text(v);

        });
    });
}

function loadUnit() {
    myGet('/api/evaluation/stats/unit', function(data){
        h = ''
        $.each(data, function(i, v){
            if (i == 0) {
                $('unit_win_rate')
            }
            h += '<div class="cp">';
            var rate = myRound(v['win_rate'],2)
    		h += '	<p class="txs32 txw1 pdb10 pdt05">'+rate+'%</p>';
            var earnSum = myRound(v['earn_unit'], 3)
    		h += '	<p>结算盈余：<span class="win">'+earnSum+'</span></p>';
    		h += '	<p>盈利'+myRound(v['win_count'], 0)+'次（'+myRound(v['win_volume'], 0)+'成交量）</p>';
    		h += '	<p>亏损'+myRound(v['lost_count'], 0)+'次（'+myRound(v['lost_volume'], 0)+'成交量）</p>	';
    		h += '	<p class="txw1 g1 pdt10">'+v['unit_start']+' ~ '+v['unit_end']+'</p>';
    		h += '</div>';
            if (i == 0) {
                $('#unit_win_rate').text(rate+'%')
                $('#unit_earn_sum').text(earnSum)
            }
        });
        $('#unit_list').html(h);
    });
}

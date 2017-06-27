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

        $('#win_lose_rate_sum').text(getWinLoseRate(data))
    });
}

function loadUnit() {
    myGet('/api/evaluation/stats/unit', function(data){
        h = '';
        $.each(data, function(i, v){

            h += '<div class="cp">';
            var rate = myRound(v['win_rate'],2);
    		h += '	<p class="txs32 txw1 pdb10 pdt05">'+rate+'%</p>';
            var earnSum = myRound(v['earn_unit'], 3);
            var clazz = earnSum > 0 ? 'win' : 'lose';
    		h += '	<p>结算盈余：<span class="'+clazz+'">'+earnSum+'</span></p>';
            var v2 = v['win_lose_rate'];
            var win_lose_rate = myRound(v2, 2) + '%';
            var clazz2 = v2 > 100 ? 'win' : 'lose';
            h += '<p>盈亏比：<span class="'+clazz2+'">'+win_lose_rate+'</span></p>';
    		h += '	<p>盈利'+myRound(v['win_count'], 0)+'次（'+myRound(v['win_volume'], 0)+'成交量）</p>';
    		h += '	<p>亏损'+myRound(v['lost_count'], 0)+'次（'+myRound(v['lost_volume'], 0)+'成交量）</p>	';
    		h += '	<p class="txw1 g1 pdt10">'+v['unit_start']+' ~ '+v['unit_end']+'</p>';
    		h += '</div>';
            if (i === 0) {
                $('#unit_win_rate').text(rate+'%');
                $('#unit_earn_sum').text(earnSum);
                $('#win_lose_rate_unit').text(win_lose_rate)
            }
        });
        $('#unit_list').html(h);
    });
}

function getWinLoseRate(data) {
    var win_lose_rate_sum = 100.0 * data.win_sum / (data.lost_sum + data.commission_sum);
    if (win_lose_rate_sum < 0) {
        win_lose_rate_sum *= -1
    }

    return myRound(win_lose_rate_sum, 2) + '%';
}

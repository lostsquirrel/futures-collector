$(function () {
    bindRange('evaluationScore');
    bindSubmit();
    loadDataList();
});

var evaluationDataUrl = '/api/evaluation/data'
function bindSubmit() {
    $('#dataForm').submit(function(){
        return false;
    })
    $('input[type="submit"]').click(function(){
        myPost(evaluationDataUrl, objectifyForm('dataForm'), function(data){
            // console.log(data)
            loadDataList();
            toasts('evalSuccess');
            fromClear('dataForm');
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
            h += '<td>'+v.position_time_str+'</td>';
            var profitClass = v.profit > 0 ? 'win' : 'lose'
            h += '<td><span class="'+(profitClass)+'">'+v.profit+'</span></td>';
            h += '<td>'+v.commission+'</td>';
            h += '<td>'+v.volume+'</td>';
            h += '<td>'+v.evaluation_score+'</td>';
            h += '<td><a href="javascript:removeData('+v.id+')" >删除</a></td>';
            h += '</tr>';
        });
        $('#dataList').append(h);
    });
}

var itemId;
$(function(){
    $('#addNode').on('click', function(){
        var itemId = $('#itemId').val();
        var ndate = $('#ndate').val();
        var open = $('#open').val();
        var close = $('#close').val();
        var lowest = $('#lowest').val();
        var highest = $('#highest').val();
        if (!itemId) {
            alert('请选择默认K线后，再添加数据！')
            return
        }
        saveNode(itemId, ndate, open, close, lowest, highest);
    });

    showItem();
    loadNodes();

});



function saveNode(itemId, ndate, open, close, lowest, highest) {
    var url = '/api/node'
    myPost(url, {item: itemId, ndate: ndate, open: open, close: close, lowest: lowest, highest: highest}, function(data){
        loadNodes();
    }, 'json');
}

function loadNodes() {
    var url = '/api/node'
    myGet(url, function(data){
        $('#list').find(".node").remove();
        var h = ''
        $(data).each(function(k, v){
            h += '<tr class="node">'
            h += '<td>'+v.date+'</td>'
            h += '<td>'+v.open+'</td>'
            h += '<td>'+v.close+'</td>'
            h += '<td>'+v.highest+'</td>'
            h += '<td>'+v.lowest+'</td>'
            h += '<td><a href="javascript:removeNode('+v.id+')" >删除</a></td>'
            h += '</tr>'
        });
        $('#list').find('tbody').append(h);
    });
}
function removeNode(id) {
    var url = '/api/node'
    myDelete(url, {id: id}, function(data){
        loadNodes();
    });
}

function showItem() {
    var url = '/api/item/default'
    myGet(url, function(data){
        var itemName = '未设定'
        if (data) {
            itemName = data.name;
            $('#itemId').val(data.id)
            itemId = data.id
        }
        $('#itemName').html(itemName)

        // addTestData();
    });
}




 $(function() {
     $('#addItem').on('click', function() {
         var name = $('#name').val();
         saveItem(name)
     });
     loadItemList();
 });

function saveItem(name) {
    myPost('/api/item', {
        name: name
    }, function(data) {
       //  console.log('------------')
        loadItemList();
    });
}

 function loadItemList() {
     var url = '/api/item'
     $('#list').find('.item').remove(); // 删除数据节点
     myGet(url, function(data) {
         var h = ''

         $(data).each(function(k, v) {

             h += '<tr class="item">'
             if (v.status == 1) {
                 h += '<th><span class="s1">当前默认</span>'+v.name+'</th>'
             } else {
                 h += '<th><a href="javascript:setDefaultItem('+v.id+')" class="a1">设为默认</a>'+v.name+'</th>';
             }
             h += '<td><a href="javascript:removeItem('+v.id+')" class="a2">删除</a></td>';
             h += '</tr>'
         });
         $('#list').append(h)
     });
 }

 function setDefaultItem(id) {
     var url = '/api/item'
     myPut(url, {id: id}, function(data){
         loadItemList();
     });
 }

 function removeItem(id) {
     var url = '/api/item'
     myDelete(url, {id: id}, function(data){
         loadItemList();
     });
 }

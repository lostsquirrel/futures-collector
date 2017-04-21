function myGet(url, callback) {
    $.get(url, callback);
}

function myPost(url, data, callback) {
    myAjax(url, 'post', data, callback);
}

function myPut(url, data, callback) {
    myAjax(url, 'put', data, callback);
}

function myDelete(url, data, callback) {
    myAjax(url, 'delete', data, callback);
}

function myAjax(url, method, data, callback) {
    $.ajax({
        url: url,
        data: JSON.stringify(data),
        success: callback,
        dataType: 'json',
        method: method,
        contentType: 'application/json; charset=UTF-8'
    });
}

function bindRange(eid) {
    $('#' + eid).on('change', function(e) {
        $('#' + eid + "Monitor").html("分数：" + $(this).val() + "分");
    });
}

function objectifyForm(fid) { //serialize data function

    var returnArray = {};
    var formArray = $('#' + fid).serializeArray()
    for (var i = 0; i < formArray.length; i++) {
        returnArray[formArray[i]['name']] = formArray[i]['value'];
    }
    return returnArray;
}

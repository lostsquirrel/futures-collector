function myGet(url, callback) {
    $.get(url, callback);
}

function myPost(url, data, callback) {
    myAjax(url, 'post',  data, callback);
}

function myPut(url, data, callback) {
 myAjax(url, 'put',  data, callback);
}

function myDelete(url, data, callback) {
    myAjax(url, 'delete',  data, callback);
}

function myAjax(url, method,  data, callback) {
    $.ajax({
        url: url,
        data: JSON.stringify(data),
        success: callback,
        dataType: 'json',
        method: method,
        contentType: 'application/json; charset=UTF-8'
    });
}

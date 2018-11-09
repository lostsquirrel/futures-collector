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
        error: errorHandler,
        dataType: 'json',
        method: method,
        contentType: 'application/json; charset=UTF-8'
    });
}
function errorHandler(e) {
    console.log("请求失败" + e)
}
function bindRange(eid) {
    $('#' + eid).on('change', function (e) {
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

function toasts(eid) {
    var item = $('#' + eid + 'Success');
    if (!item.length) {
        item = $('<span class="pdl20 b1" id="' + eid + 'Success" style="display:none">保存成功！</span>');
        $('#' + eid).parent().append(item);
    }
    item.show();
    setTimeout(function () {
        item.hide();
    }, 3000);
}

function fromClear(formId) {
    var tForm = $('#' + formId);
    tForm.find("input[type=text], textarea").val("");
    tForm.find('input[type=range]').val(0);
    tForm.find('input[type=radio]').prop('checked', false);
}

function myRound(n, d) {
    return Number( Number(n).toFixed(d)).toString();
}

function isInt(n) {
    return n % 1 === 0;
}

function isFloadOne(n) {
    return n % 0.1 === 0;
}

function isFloadTwo(n) {
    return n % 0.01 === 0;
}
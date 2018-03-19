/**
 * Description：公用js-api
 *
 * @author : xutao
 * Created_Date : 2017-11-07 14:36
 */
// 获取屏幕实际显示高度
function getClientHeight() {
  let clientHeight = 0;
  if (document.body.clientHeight && document.documentElement.clientHeight) {
    clientHeight = (document.body.clientHeight < document.documentElement.clientHeight) ? document.body.clientHeight : document.documentElement.clientHeight;
  } else {
    clientHeight = (document.body.clientHeight > document.documentElement.clientHeight) ? document.body.clientHeight : document.documentElement.clientHeight;
  }
  return clientHeight;
}

// 获取屏幕实际显示宽度
function getClientWidth() {
  let clientWidth = 0;
  if (document.body.clientWidth && document.documentElement.clientWidth) {
    clientWidth = (document.body.clientWidth < document.documentElement.clientWidth) ? document.body.clientWidth : document.documentElement.clientWidth;
  } else {
    clientWidth = (document.body.clientWidth > document.documentElement.clientWidth) ? document.body.clientWidth : document.documentElement.clientWidth;
  }
  return clientWidth;
}

// 目标字符串是否为空
function isBlank(target) {
  return target === null || target === undefined || target === '';
}

// 设置cookie值
function setCookie(key, value, expireDays, domain, path) {
  let exdate = new Date();
  exdate.setDate(exdate.getDate() + expireDays);
  document.cookie = key + "=" + escape(value)
    + ((isBlank(expireDays)) ? "" : ";expires=" + exdate.toGMTString())
    + ((isBlank(domain)) ? "" : ";domain=" + domain)
    + ((isBlank(path)) ? "" : ";path=" + path);
}

// 读取cookie值
function getCookie(key) {
  if (document.cookie.length > 0) {
    let startIndex = document.cookie.indexOf(key + "=");
    if (startIndex !== -1) {
      startIndex = startIndex + key.length + 1;
      let endIndex = document.cookie.indexOf(";", startIndex);
      if (endIndex === -1) {
        endIndex = document.cookie.length;
      }
      return unescape(document.cookie.substring(startIndex, endIndex));
    }
  }
  return "";
}

// 删除cookie
function delCookie(name) {
  let exp = new Date();
  exp.setTime(exp.getTime() - 1);
  let val = getCookie(name);
  if (val !== null) {
    document.cookie = name + "=" + val + ";expires=" + exp.toGMTString();
  }
}

// 获取url中携带的请求参数
function getRequestParam() {
  let request = {};
  //获得URL问号后面的字符串，包括问号
  let param = window.location.search;
  if (param !== '') {
    //去掉问号
    param = param.substring(1);
    //用‘&’，分离出带有的参数
    let params = param.split("&");
    //用‘=’，循环将参数分离成key-value形式，并封装到对象中
    for (let i = 0; i < params.length; i++) {
      let kv = params[i].split("=");
      request[kv[0]] = kv[1];
    }
  }
  return request;
}

// 公用ajax请求
function ajaxReq(url, paramObj, successCallback, errorCallBack) {
  paramObj['st'] = getCookie('st');// 会话token请求必推
  $.ajax({
    type: "POST",
    url: url,
    contentType: 'application/json;charset=utf-8',
    dataType: 'json',
    data: JSON.stringify(paramObj),
    success: function (result) {
      if (successCallback) {
        successCallback(result);
      } else {
        // do nothing
      }
    },
    error: function (e) {
      if (errorCallBack) {
        errorCallBack(e);
      } else {
        alert("请求失败 , 请重试 :-)");
      }
    }
  });
}

// 跳转对应url
function goto(url) {
  window.location.href = url;
}

// localStorage set
function setStorage(key, val) {
  window.localStorage.setItem(key, val);
}

// localStorage get
function getStorage(key) {
  return window.localStorage.getItem(key);
}

// localStorage remove
function delStorage(key) {
  window.localStorage.removeItem(key);
}

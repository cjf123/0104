//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    motto: '基础视图View，滑动视图ScrollView，滑块Swiper',
    info: '更多教程和源码请关注51小程序：http://html51.com/',
    userInfo: {}
  },

  onLoad: function () {
    console.log('onLoad')
    var that = this
    //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
  }
})

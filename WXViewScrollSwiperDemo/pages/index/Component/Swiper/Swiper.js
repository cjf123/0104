//Swiper.js
Page({
  data: {
    background: ['green', 'red', 'yellow'],
    indicatorDots: true,    //布尔值变量，用于控制显示/取消指示点
    vertical: false,        //根据这个布尔值的真假，控制滑块视图，横显示或者竖显示
    autoplay: false,        //通过这个开关控制，是否开始轮播，或者停止轮播
    interval: 3000,         //设置间隔多长时间显示下一个图
    duration: 1200          //设置轮播一次的时间
  },
  changeIndicatorDots: function (e) {
    this.setData({
      indicatorDots: !this.data.indicatorDots
    })
  },
  changeVertical: function (e) {
    this.setData({
      vertical: !this.data.vertical
    })
  },
  changeAutoplay: function (e) {
    this.setData({
      autoplay: !this.data.autoplay
    })
  },
  intervalChange: function (e) {
    this.setData({
      interval: e.detail.value
    })
  },
  durationChange: function (e) {
    this.setData({
      duration: e.detail.value
    })
  }
})
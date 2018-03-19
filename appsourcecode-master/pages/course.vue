<template>
  <div id="course">
    <mt-swipe :auto="4000">
      <mt-swipe-item>
        <router-link :to="{path:'/job'}"><img src="../assets/images_home/banner1.jpg"></router-link>
      </mt-swipe-item>
      <mt-swipe-item>
        <router-link :to="{path:'/course'}"><img src="../assets/images_home/banner2.jpg"></router-link>
      </mt-swipe-item>
      <mt-swipe-item>
        <router-link :to="{path:'/teacher'}"><img src="../assets/images_home/banner3.jpg"></router-link>
      </mt-swipe-item>
    </mt-swipe>
    <ul class="course-article">
      <mt-loadmore :top-method="loadTop" :bottom-method="loadBottom" ref="loadmore">
        <router-link v-for="cont in course" :to="{path:cont.rout}">
          <li>
            <div class="text">
              <div><img :src="cont.logo"></div>
              <div>
                <h3>{{cont.title}}</h3>
                <p>{{cont.text}}</p>
              </div>
            </div>
          </li>
        </router-link>
      </mt-loadmore>
    </ul>
  </div>
</template>
<script>
  import '../../static/css/course.css'
  import {Loadmore} from 'mint-ui';

  export default {
    data() {
      return {
        course: [
          {
          	rout: 'Youer',
            title: '幼儿英语',
            logo: require("../../static/img/youer.jpg"),
            text: '幼儿英语幼儿英语幼儿英语幼儿英语幼儿英语幼儿英语幼儿英语幼儿英语幼儿英语'
          },
          {
          	rout: 'Shaoer',
            title: '青少儿英语',
            logo: require("../../static/img/ertong.jpg"),
            text: '青少儿英语青少儿英语青少儿英语青少儿英语青少儿英语青少儿英语青少儿英语'
          },
          {
          	rout:'zhongxue',
            title: '中学英语',
            logo: require("../../static/img/zhongkao.jpg"),
            text: '中学英语中学英语中学英语中学英语中学英语中学英语中学英语'
          },
          {
          	rout:'HightSchool',
            title: '高中英语',
            logo: require("../../static/img/gaokao.jpg"),
            text: '高中英语高中英语高中英语高中英语高中英语高中英语高中英语高中英语'
          },
          {
          	rout:'yasi',
            title: '雅思新托福',
            logo: require("../../static/img/yasi.jpg"),
            text: '雅思新托福雅思新托福雅思新托福雅思新托福雅思新托福雅思新托福'
          },
          {
          	rout:'Oral',
            title: '口译口语',
            logo: require("../../static/img/kouyu.jpg"),
            text: '口译口语口译口语口译口语口译口语口译口语口译口语口译口语口译口语'
          },
          {
          	rout:'CET',
            title: '英语四六级',
            logo: require("../../static/img/siliuji.jpg"),
            text: '英语四六级英语四六级英语四六级英语四六级英语四六级英语四六级'
          },
          {
          	rout:'TEM',
            title: '专业四八级',
            logo: require("../../static/img/zhuanye8.jpg"),
            text: '专业四八级专业四八级专业四八级专业四八级专业四八级专业四八级'
          }
        ]
      }
    },
    methods: {
      loadTop() {
        // 加载更多数据
        this.$refs.loadmore.onTopLoaded();
      },
      allLoaded() {
        // 加载更多数据
        this.$refs.loadmore.onTopLoaded();
      },
      loadBottom() {
        // 加载更多数据
        this.allLoaded = true;// 若数据已全部获取完毕
        this.$refs.loadmore.onBottomLoaded();
      }
    }
  }
</script>

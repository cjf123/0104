<template>
  <div id="footer">
    <router-link :to="{path:'/From'}">
      <span><img src="../assets/images_home/tab_iocn_62.png">申请试听</span>
    </router-link>
    <span @click="call"><img src="../assets/images_home/tab_iocn_64.png">联系电话</span>
    <span><img src="../assets/images_home/tab_iocn_66.png">联系我们</span>
  </div>
</template>
<script>
  import '../../static/css/foot.css'
  import {MessageBox} from 'mint-ui';

  export default {
    data() {
      return {
        num: '17858753829'
      }
    },
    methods: {
      call() {
        MessageBox({
          title: '',
          message: this.num,
          confirmButtonText: '拨打电话'
        }).then(action => {
          window.location.href = 'tel://' + this.num
        });
      }
    }
  }
</script>
<style>
  #nav a {
    color: #2c3e50;
    text-decoration: none
  }

  #nav a.router-link-active {
    color: #c01920
  }
</style>

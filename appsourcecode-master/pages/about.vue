<template>
  <div class="about">
    <div class="banner">
      <img src="../assets/images_women/tupian_02.png">
    </div>
    <div class="about-article">
      <h2>向日葵英语介绍</h2>
      <h4>GROUP INTRODUCTION</h4>
      <p>
      	<img src="../assets/images_home/reason_img1.jpg" alt="" />
      	<span>优秀的师资团队</span>
        <img src="../assets/images_home/reason_img2.jpg" alt="" />
        <span>深远的企业文化</span>
        <img src="../assets/images_home/reason_img3.jpg" alt="" />
        <span>舒适的公司环境</span>
      </p>
      <router-link :to="{path:'/introduce'}">
        <div class="introduce">查看详情</div>
      </router-link>
    </div>
  </div>
</template>
<script>
  import '../../static/css/about.css'
</script>
<style></style>

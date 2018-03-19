<template>
  <div class="about-me-block">
    <div>
      <h1 class="about-me-title">关于我</h1>
      你好!<br/>
      我是Blue<br/>
      欢迎浏览此博客<br/>
      这里有一些本人原创的<br/>
      或用作分享的<br/>
      技术类文章及资源<br/>
      也有一些<br/>
      本人平日里<br/>
      无处发泄的小牢骚<br/>
      任何问题<br/>
      欢迎联络<br/>
      祝好!
    </div>
  </div>
</template>

<script>
  export default {
    name: 'aboutMe',
    data: function () {
      return {}
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .about-me-block {
    height: 100%;
    display: flex;
    display: -webkit-flex; /* Safari */
    align-items: center; /*指定垂直居中*/
    justify-content: center;
    color: #F8F6D2;
    font-size: 18px;
    text-shadow: 1px 1px 1px #4c4c4c;
  }

  .about-me-title {
    margin-bottom: 20px;
  }
</style>

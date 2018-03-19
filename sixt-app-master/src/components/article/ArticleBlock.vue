<template>
  <div class="article-block">
    <div class="header">
      <a class="article-title-link" href="#" title="测试标题">
        我是标题
      </a>
    </div>
    <div class="article-preview-img">
      <img class="preview-img" src="../../assets/img-test.jpg"/>
    </div>
    <div class="article-guide-cnt">
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
      我是文章我是文章我是文章我是文章我是文章我是文章<br/>
    </div>
    <div class="toolkit-block">

    </div>
  </div>
</template>

<script>
  export default {
    name: 'articleBlock',
    data: function () {
      return {}
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .article-block {
    background-color: #fff;
    margin: 20px auto;
    border: 1px solid #DDDDDD;
  }

  .header {
    width: 100%;
    height: 80px;
    line-height: 80px;
    padding-left: 32px;
    border-left: 8px solid #4D4D4D;
  }

  .article-title-link {
    display: inline-block;
    text-decoration: none;
    color: #696969;
    font-size: 24px;
    font-family: "Microsoft JhengHei", "Microsoft YaHei", "Trebuchet MS", Arial, Verdana, Tahoma, sans-serif !important;
  }

  .article-preview-img {
    padding: 10px 40px;
  }

  .preview-img {
    max-width: 100%;
  }

  .article-guide-cnt {
    padding: 20px 40px;
  }

  .toolkit-block {
    margin: 10px 40px 20px 40px;
    border-top: 1px solid #DDDDDD;
  }
</style>

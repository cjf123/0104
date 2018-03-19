<template>
  <div class="article-btn">
    <div class="line-title">
      <i class="icon-quote-left iconfont">&#xe67b;</i>
      <a class="link-title link" href="javascript:void(0)" title="文章标题" slot="title">
        <slot>浅谈mvc模式</slot>
      </a>
    </div>
    <div class="line-info">
      <i class="iconfont">&#xe63e;</i>
      <a class="link-date link" href="javascript:void(0)" slot="date">
        <slot>2018-01-01</slot>
      </a>

      <i class="iconfont">&#xe68a;</i>
      <a class="link-tag link" href="javascript:void(0)" slot="tag">
        <slot>标签</slot>
      </a>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'articleBtn',
    data: function () {
      return {}
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .article-btn {
    color: #fff;
    text-shadow: 1px 1px 1px #545454;
    height: 50px;
    border-bottom: 1px dotted #fff;
    padding: 10px 4px 10px;
  }

  .article-btn:hover {
    background-color: rgba(255, 255, 255, .2);
  }

  .icon-quote-left {
    color: #FEFDDB;
    font-size: 20px;
    margin-right: 5px;
  }

  .line-title {
    font-size: 18px;
    height: 25px;
    line-height: 25px;
    overflow: hidden;
  }

  .line-title:hover {
    cursor: pointer;
  }

  .link {
    text-decoration: none;
    color: #FEFDDB;
  }

  .link-date {
    margin-right: 10px;
  }

  .link-title {
    color: #fff;
  }

  .line-info .iconfont {
    color: #FEFDDB;
  }

  .line-info {
    font-size: 15px;
  }
</style>

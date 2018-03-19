<template>
  <div class="nav-block">
    <ul>
      <li><a href="#">主页</a></li>
      <li><a href="#">相册</a></li>
      <li><a href="#">文件</a></li>
      <li><a href="#">友链</a></li>
    </ul>

    <ul class="rowUl">
      <li>-</li>
      <li><a href="javascript:void(0)" @click="catalogClick">类目</a></li>
      <li>-</li>
      <li><a href="javascript:void(0)" @click="aboutMeClick">Me</a></li>
      <li>-</li>
    </ul>
    <div class="clearfix"></div>
  </div>
</template>

<script>
  export default {
    name: 'navBlock',
    data: function () {
      return {}
    },
    methods: {
      aboutMeClick: function () {
        this.$emit('showIntroBlock');
      },
      catalogClick: function () {
        this.$emit('showCatalogBlock');
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .nav-block {
    text-align: center;
  }

  .nav-block ul li {
    padding: 5px 0;
  }

  .nav-block ul li a {
    color: #898989;
    font-size: 16px;
    line-height: 16px;
  }

  .nav-block ul li a:hover {
    color: #25B887;
  }

  .rowUl {
    margin-left: 93px;
  }

  .rowUl li {
    float: left;
    margin: 10px 3px 0;
  }

  .rowUl li a {
    font-size: 14px !important;
    line-height: 14px !important;
    padding: 2px 4px !important;
  }
</style>

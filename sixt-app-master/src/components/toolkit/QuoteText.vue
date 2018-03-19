<template>
  <div class="quote-text">
    <div class="quote-left"></div>
    <slot>
      我是默认文字 , 被你看到还真是不好意思~ (娇羞脸)
    </slot>
    <div class="quote-right"></div>
  </div>
</template>

<script>
  export default {
    name: 'quoteText',
    data: function () {
      return {}
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .quote-text {
    font-family: "Microsoft JhengHei", "Microsoft YaHei", "Trebuchet MS", Arial, Verdana, Tahoma, sans-serif !important;
    font-size: 16px !important;
    color: #9D9D9D !important;
  }

  .quote-left {
    width: 15px;
    height: 15px;
    display: inline-block;
    background-image: url("../../assets/quote-left.png");
    background-size: 15px 15px;
    margin-right: 5px;
  }

  .quote-right {
    width: 15px;
    height: 15px;
    display: inline-block;
    background-image: url("../../assets/quote-right.png");
    background-size: 15px 15px;
    margin-left: 5px;
  }
</style>

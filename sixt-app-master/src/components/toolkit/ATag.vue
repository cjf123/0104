<template>
  <div class="tag-block" @click="tagClick">
    <i class="iconfont">&#xe6bf;</i>
    <slot style="vertical-align: middle">默认标签</slot>
  </div>
</template>

<script>
  export default {
    name: 'aTag',
    data: function () {
      return {}
    },
    methods: {
      tagClick: function () {
        console.log("tag click");
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .tag-block {
    display: inline-block;
    width: auto;
    height: 25px;
    color: #fff;
    font-size: 14px;
    line-height: 25px;
    padding: 0 6px;
    border-radius: 4px;
    margin: 2px;
  }

  .tag-block:hover {
    color:#FDFDDE;
    text-shadow: 1px 1px 1px #767676;
    cursor: pointer;
  }

</style>

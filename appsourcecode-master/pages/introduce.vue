<template>
  <div>
    <div class="about">
      <h2>向日葵英语介绍绍</h2>
      <h4>GROUP INTRODUCTION</h4>
      <p>向日葵英语介绍详细信息</p>
    </div>
    <div @click="back">返回</div>
  </div>
</template>
<script>
  export default {
    methods:{
      back(){
        this.$router.go(-1)
      }
    }
  }
</script>


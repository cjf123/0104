<template>
 	<div>
		<div class="title course-title">
			<div class="back mintui mintui-back" @click="back">返回</div>
			<h3>高中英语</h3>
			<div class="line1"></div>
			<div class="line2"></div>
		</div>
		<!--<div class="course-nav">
			<span class="active">课程特色</span>
			<span>学习系统</span>
			<span>国际教材</span>
			<span>学习成果</span>
		</div>-->
		<div id="course-nav">
			<mt-navbar v-model="selected" class="course-nav">
      <mt-tab-item id="1">课程特色</mt-tab-item>
      <mt-tab-item id="2">学习系统</mt-tab-item>
      <mt-tab-item id="3">国际教材</mt-tab-item>
      <mt-tab-item id="4">学习成果</mt-tab-item>
    </mt-navbar>
		</div>

		<div class="course-introduce">
			<div class="banner"><img src="../../../static/img/youerEnglish.jpg" alt=""></div>
			<p>
				这个阶段幼儿英语教学目的是从小培养良好幼儿英语语感，同时注重社交、认知等综合能力的培养。英孚教育基于对中国大量3到6岁幼儿的研究，推出了4套针对不同年龄幼儿认知特点和学习习惯的教案，同时提供全套帮助父母在家里营造英语环境的工具，在课内课外给孩子最全面有效的幼儿英语培训系统。
			</p>
		</div>
	</div>
</template>
<script>
	import {Navbar, TabItem} from 'mint-ui'
  import {MessageBox} from 'mint-ui'
  import '../../../static/css/home.css'
  export default {
    data(){
      return{
        selected:'1'
      }
    },
    methods: {
      back() {
        this.$router.go(-1)
      }
    }
  }
</script>
<style>
</style>

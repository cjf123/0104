<template>
	<div class="our">
		<div class="banner">
			<img src="../../static/img/school-banner.jpg"/>
			<div class="banner-cont">
				<h3>每一次上课，都有新收获</h3>
				<div class="line1"></div>
				<p>助学员拥有美好的未来</p>
			</div>
			
		</div>
		<div class="talk-show">
			<h3>向日葵零零后英语脱口秀</h3>
			<div class="line3"></div>
			<p>向日葵教育零零后英语脱口秀特别邀请向日葵的小学员录制视频，以真人+动画的生动形式讲解实用的英语单词和词组，让孩子Fun学英语！小学员的自信表达、纯正口音对同龄孩子的英语学习起到积极的榜样作用。</p>
		</div>
		<button>
      <router-link :to="{path:'/From'}">点击立即体验课程，让宝贝也拥有一口流利英语</router-link>
    </button>
    <div class="shaoerzu">
    	<h2>少儿组风采</h2>
		    <div class="line1"></div>
		    <div class="line2"></div>
				<ul class="our-article">
					<li v-for="cont in student">
						<div class="text">
							<div class="pic"><img :src="cont.pic" alt="" /></div>
							<h3>{{cont.name}}</h3>
							<p>{{cont.age}}</p>
						</div>
					</li>
				</ul>
    </div>
    
	</div>
</template>
<script>
	import '../../static/css/our.css'

	export default {
		data() {
			return {
				student: [
					{
						pic:require("../../static/img/talkshow1.jpg"),
						name: '幼儿英语学员',
						age: '6岁'
					},
					{
						pic:require("../../static/img/talkshow2.jpg"),
						name: '幼儿英语学员-Zoe',
						age: '5岁'
					},{
						pic:require("../../static/img/talkshow3.jpg"),
						name: '幼儿英语学员-Sunny',
						age: '6岁'
					},{
						pic:require("../../static/img/talkshow4.jpg"),
						name: '少儿英语学员-Ella',
						age: '9岁'
					},
					{
						pic:require("../../static/img/talkshow5.jpg"),
						name: '幼儿英语学员-Vanessa',
						age: '4岁'
					},
					{
						pic:require("../../static/img/talkshow6.jpg"),
						name: '少儿英语学员-Yoka',
						age: '10岁'
					},
					{
						pic:require("../../static/img/talkshow7.jpg"),
						name: '幼儿英语学员',
						age: '6岁'
					},
					{
						pic:require("../../static/img/talkshow8.jpg"),
						name: '少儿英语学员-Angel',
						age: '9岁'
					}
				]
			}
		}
	}
</script>
<template>
	<div class="teacher">
		<div class="banner">
			<img src="../../static/img/teacher-banner2.jpg" />
			<div class="banner-cont">
				<h3>外籍培训师</h3>
        <div class="line1"></div>
        <p>专业的培训师团队接受过<br/>严格面试、全面培训，掌握前沿的教学方法。</p>
			</div>
		</div>
		<ul class="teacher-article">
			<li v-for="cont in teacher">
				<div class="text">
					<div><img :src="cont.logo"></div>
					<div>
						<span class="clear">
              <h3>{{cont.names}}</h3>
              <h4>{{cont.title}}</h4>
            </span>
						<p>{{cont.text}}</p>
					</div>
				</div>
			</li>
		</ul>
	</div>
</template>
<script>
	import '../../static/css/teacher.css'

	export default {
		data() {
			return {
				teacher: [{
						names: '培训师 Saien Gopalan',
						title: '/ 我的祖先来自南非，我的改变来自教育',
						logo: require('../assets/images_shizi/saien-hd.jpg'),
						text: '28岁的SAIEN GOPALAN（以下简称SAI）来自南非的一个典型“书香门第”，每位家庭成员都接受过高等教育。他说，在许多年前，外公那个时代，教育并不被人们重视，SAI的外公也因为家庭原因与教育失之交臂。“教育依然是他的情结，三十年前，即使教育观念还不那么普及，”SAI说道，“我的母亲在外公的教导下，成为了全家第一个读完高中的人。”'
					},
					{
						names: '培训师 Simin',
						title: '/ 我是女生',
						logo: require('../assets/images_shizi/simin-hd.jpg'),
						text: 'SIMIN说，她非常喜欢自己的工作，因为在这里不仅仅是她去教学生，自己也可以学到很多，甚至有了机会可以去学习机会难得的 DIPTESOL 课程（DIPTESOL 是被全球认可的高级教师专业资格证）。这种双向的学习让她整个人都充满干劲。'
					},
					{
						names: '培训师 Saien Gopalan',
						title: '/ 我的祖先来自南非，我的改变来自教育',
						logo: require('../assets/images_shizi/saien-hd.jpg'),
						text: '28岁的SAIEN GOPALAN（以下简称SAI）来自南非的一个典型“书香门第”，每位家庭成员都接受过高等教育。他说，在许多年前，外公那个时代，教育并不被人们重视，SAI的外公也因为家庭原因与教育失之交臂。“教育依然是他的情结，三十年前，即使教育观念还不那么普及，”SAI说道，“我的母亲在外公的教导下，成为了全家第一个读完高中的人。”'
					},
					{
						names: '培训师 Simin',
						title: '/ 我是女生',
						logo: require('../assets/images_shizi/simin-hd.jpg'),
						text: 'SIMIN说，她非常喜欢自己的工作，因为在这里不仅仅是她去教学生，自己也可以学到很多，甚至有了机会可以去学习机会难得的 DIPTESOL 课程（DIPTESOL 是被全球认可的高级教师专业资格证）。这种双向的学习让她整个人都充满干劲。'
					}
				]
			}
		}
	}
</script>
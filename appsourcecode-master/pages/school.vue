<template>
	<div class="school">
		<div class="banner">
			<img src="../../static/img/school-banner.jpg" />
			<div class="banner-cont">
				<h3>每一次上课，都有新收获</h3>
				<div class="line1"></div>
				<p>交通便利的多媒体互动语音教室，<br/>让英语学习快捷又有趣。</p>
			</div>
		</div>
		<ul class="school-article">
			<li v-for="cont in school">
				<div class="text">
					<div>
						<h3>{{cont.title}}</h3>
						<p>{{cont.text}}</p>
						<p>{{cont.phone}}</p>
						<p>{{cont.car}}</p>
					</div>
				</div>
			</li>
		</ul>
	</div>
</template>
<script>
	import '../../static/css/school.css'

	export default {
		data() {
			return {
				school: [{
						title: '湖滨中心',
						text: '杭州市延安路258号湖滨银泰二期B332',
						phone: '电话：400 656 7890, 800 656 7890',
						car: '交通:地铁：1号线龙翔桥站，D4号口。 公交:7,27,52,56,504'
					},
					{
						title: '城西中心',
						text: '杭州市拱墅区丰潭路430号丰元国际大厦A座2楼',
						phone: '电话：400 656 7890, 800 656 7890',
						car: '交通:地铁：1号线龙翔桥站，D4号口。 公交:7,27,52,56,504'
					},
					{
						title: '武林中心',
						text: '杭州市下城区环城北路208号坤和中心902-903',
						phone: '电话：400 656 7890, 800 656 7890',
						car: '交通:地铁：1号线龙翔桥站，D4号口。 公交:7,27,52,56,504'
					},
					{
						title: '滨江中心',
						text: '滨江区江南大道228号星光国际广场1号楼4层',
						phone: '电话：400 656 7890, 800 656 7890',
						car: '交通:地铁：1号线龙翔桥站，D4号口。 公交:7,27,52,56,504'
					},
					{
						title: '西溪印象城中心',
						text: '杭州市余杭区五常大道1号西溪印象城4层P1-04-01a2商铺',
						phone: '电话：400 656 7890, 800 656 7890',
						car: '交通:地铁：1号线龙翔桥站，D4号口。 公交:7,27,52,56,504'
					}
				]
			}
		}
	}
</script>
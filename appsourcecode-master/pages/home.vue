<template xmlns="">
  <div class="home">
    <mt-swipe :auto="4000">
      <mt-swipe-item>
        <router-link :to="{path:'/job'}"><img src="../assets/images_home/banner1.jpg"></router-link>
      </mt-swipe-item>
      <mt-swipe-item>
        <router-link :to="{path:'/course'}"><img src="../assets/images_home/banner2.jpg"></router-link>
      </mt-swipe-item>
      <mt-swipe-item>
        <router-link :to="{path:'/teacher'}"><img src="../assets/images_home/banner3.jpg"></router-link>
      </mt-swipe-item>
    </mt-swipe>
    <div class="title">
      <h3>我们的课程</h3>
      <div class="line1"></div>
      <div class="line2"></div>
      <p>帮助不同英语层次的求学者高效掌握英语！</p>
    </div>

    <div class="course">
      <span><router-link :to="{path:'/Youer'}"><img src="../../static/img/youer.jpg">幼儿英语</router-link></span>
      <span><router-link :to="{path:'/Shaoer'}"><img src="../../static/img/ertong.jpg">青少儿英语</router-link></span>
      <span><router-link :to="{path:'/Zhongxue'}"><img src="../../static/img/zhongkao.jpg">中学英语</router-link></span>
      <span><router-link :to="{path:'/HightSchool'}"><img src="../../static/img/gaokao.jpg">高中英语</router-link></span>
      <span><router-link :to="{path:'/Yasi'}"><img src="../../static/img/yasi.jpg">雅思新托福</router-link></span>
      <span><router-link :to="{path:'/Oral'}"><img src="../../static/img/kouyu.jpg">口译口语</router-link></span>
      <span><router-link :to="{path:'/CET'}"><img src="../../static/img/siliuji.jpg">英语四六级</router-link></span>
      <span><router-link :to="{path:'/TEM'}"><img src="../../static/img/zhuanye8.jpg">专业四八级</router-link></span>
    </div>
    <div class="title choice">
      <h3>选择我们的理由</h3>
      <div class="line1"></div>
      <div class="line2"></div>
      <p>全球先进英语培训专家,专业的领导团队</p>
    </div>
    <div class="reason">
      <ul>
        <li>
          <span>
            <img src="../assets/images_home/reason_img1.jpg" alt="">
          </span>
          <div class="article">
            <h4>向日葵专业的师资团队<br/>深耕中国，成果卓著</h4>
            <p>
              <strong>向日葵教育</strong>从学术资格和职业性格精选英语培训师,优秀的英语培训师够让孩子们在欢笑中燃起学习兴趣。针对3-6岁幼儿英语学习者，我们更培训了一批来自专业助教辅助教学，帮助孩子们轻松融入英语学习环境。
            </p>
            <span>
              <router-link to="/about">了解更多向日葵品牌故事>></router-link>
            </span>
          </div>
        </li>
        <li>
          <span>
            <img src="../assets/images_home/reason_img2.jpg" alt="">
          </span>
          <div class="article">
            <h4>面对不同英语需求的求学者<br/>先进的英语教学技术</h4>
            <p>
              <strong>向日葵教育</strong>教学研发部门专注于改进英语学习方法。通过不断研发先进的课堂多媒体技术、在线互动英语学习系统、智能手机学习应用和持续的课程进度追踪系统，为学生提供良好的学习效果。
            </p>
            <span>
              <router-link to="/course">了解向日葵口碑课程>></router-link>
            </span>
          </div>
        </li>
        <li>
          <span>
            <img src="../assets/images_home/reason_img3.jpg" alt="">
          </span>
          <div class="article">
            <h4>全球英语培训品牌<br/>便利的英语培训中心位置</h4>
            <p>
              <strong>向日葵教育</strong>英语培训中心遍布全球，向日葵根据中国学员的语言学习习惯，专门研发了一整套专业的英语教学体系和教学方法。目前，向日葵在全球各地拥有众多英孚英语培训中心和办事处组成了向日葵英语教育网络。
            </p>
            <span>
              <router-link to="/school">了解校区地址>></router-link>
            </span>
          </div>
        </li>
      </ul>
      <button>
        <router-link :to="{path:'/From'}">马上体验向日葵国际化课程 >></router-link>
      </button>
    </div>
    <mt-navbar v-model="selected">
      <mt-tab-item id="1">{{newsTitle}}</mt-tab-item>
      <mt-tab-item id="2">{{newsTitle2}}</mt-tab-item>
    </mt-navbar>

    <!-- tab-container -->
    <mt-tab-container v-model="selected">
      <mt-tab-container-item id="1">
        <router-link v-for="(n,index1) in cont1" :to="{name:'News',params:{cont1,index1}}">
          <mt-cell v-if="index1<4" :title="n.title"/>
        </router-link>
      </mt-tab-container-item>
      <mt-tab-container-item id="2">
        <router-link v-for="(n,index2) in cont2" :to="{name:'News1',params:{cont2,index2}}">
          <mt-cell v-if="index2<4" :title="n.title"/>
        </router-link>
      </mt-tab-container-item>
    </mt-tab-container>
    <div class="more-news">[ 更多 ]</div>
    <div class="top">
      <img src="../assets/images_home/line_1px_42.png" alt="">
    </div>
    <div class="foot">
      <p>版权所有：向日葵英语培训有限公司 浙ICP备11111111号</p>
    </div>
  </div>
</template>
<script>
  import '../../static/css/home.css'
  import {Navbar, TabItem} from 'mint-ui'
  import {MessageBox} from 'mint-ui';

  export default {
    data() {
      return {
        selected: '1',
        newsTitle: '向日葵活动',
        newsTitle2: '英语学习角',
        cont1: [
          {
            title: '向日葵少儿英语趣味大比拼！-向日葵教育',
            time: '2017-10-11',
            text: '<div><img src="../../static/img/art1.jpg" width="100%"><img src="../../static/img/art2.jpg" width="100%"><img src="../../static/img/art3.jpg" width="100%"></div>'
          },
          {
            title: '儿童英语如何高效学习？-向日葵教育',
            time: '2017-10-12',
            text: '<div><img src="../../static/img/art4.jpg" width="100%"><p>儿童英语学习是家长们比较重视的事情，家长呢经常会从幼儿时期就会对孩子进行英语启蒙，但很多家长可能没有很好的外语基础，而儿童英语学习需要很好的语言学习环境只有在一定的英语语言环境中，孩子才能学会应用英语，进而学好英语。</p><img src="../../static/img/art5.jpg" width="100%"><p>国际语言专家说：孩子再0到3岁时期是学习一门语言的零困难期。所以这个时期除了要教孩子学习汉语外更要给孩子一定的英语语言刺激，让孩子从小接触英语，幼儿英语学习不在于能学多少英语单词，英语语法，更多的是培养孩子对英语的兴趣。</p><img src="../../static/img/art6.jpg" width="100%"><p>有些家长会问，幼儿时期即学英语又学汉语会不会弄混淆呢？</p><img src="../../static/img/art7.jpg" width="100%"><p>这个完全不用担心，我们在电脑经常会看到明星的孩子既会说汉语又会说英语，粤语等，就像杨幂的女儿，不到三岁就会说三种语言。母语跟外语是两个不用的语言系统，孩子在学习语言时是分两个系统进行学习的，大脑中也会分两个不同的系统记忆不同的语言知识。由此可见孩子再幼儿时期学习语言完全不用担心。</p><img src="../../static/img/art8.jpg" width="100%"><p>所以，幼儿英语启蒙非常重要，家长们在家可以简单的和孩子进行英语交流。这样孩子学习效率会高很多哦！</p></div>'
          },
          {
            title: '向日葵英语秋季班开抢啦！',
            time: '2017-8-11',
            text: '<div>' +
            '<p>艾瑞巴蒂，2017已走过四分之三，秋意越来越浓，感觉就要过冬的节奏，过完了2017年所有法定节假日，最让孩子们翘首以盼的莫过于寒假啦！<br/>寒假太短，不想出游？忙碌了一个学期，不想让孩子的寒假太辛苦？好好学习了一学期，又不想寒假太放松？<br/>亲爱的粑粑麻麻，是时候未雨绸缪、抢夺先势了。站在机会面前，你需要：<br/></p>' +
            '<p style="text-align: center">还有就是趁现在！！<br/>报寒假班这种事，<br/>当然是选择向日葵！<br/>这个冬天，向日葵英语寒假班全面升级！<br/>自然拼读奇趣营<br/>快乐母语教学，告别死记硬背！</p><img src="../../static/img/UE.jpg" width="100%">' +
            '<div class="course1">' +
            '<div class="art1"><img src="../../static/img/youer.jpg"><h5>幼儿英语</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>' +
            '<div class="art1"><img src="../../static/img/ertong.jpg"><h5>青少儿英语</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>' +
            '<div class="art1"><img src="../../static/img/zhongkao.jpg"><h5>中学英语</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>' +
            '<div class="art1"><img src="../../static/img/gaokao.jpg"><h5>高中英语</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>' +
            '<div class="art1"><img src="../../static/img/yasi.jpg"><h5>雅思新托福</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>' +
            '<div class="art1"><img src="../../static/img/kouyu.jpg"><h5>口译口语</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>' +
            '<div class="art1"><img src="../../static/img/siliuji.jpg"><h5>英语四六级</h5><p>课程特色<br/>1. 世上绝大多数的单词可以通过自然拼读法轻松掌握！英孚特色的母语式教学，帮助孩子通过学习字母和发音的对应联系，准确发音，学习拼读单词，告别传统英语学习死记硬背记单词的痛苦，让学单词更轻松。<br/>2. 科学设置教案，采用英语国家在孩子启蒙阶段的英语教学法，把复杂的发音归纳成有规律的、简单的发音，不同于传统国际音标，更适合英语初学者。<br/>3. 针对不同年龄段的儿童学习语言的特点，通过直接学习26个字母及字母组合在单词中的发音规则，建立字母及字母组合如何发音的感知，从而层层递进地系统性学习音素、音位、语音系统和自然拼读法。<br/>招募对象：3-6岁</p></div>'
          },
          {
            title: '向日葵新创专业的英语学习系统',
            time: '2017-8-11',
            text: '<div class="course2"><img src="../../static/img/course-overview-circle.png"><p>向日葵 Smart 15 学习系统<br/>向日葵 Smart 15系统能够帮助您学习现<br/>实生活中用得到的英语。“学习—尝试<br/>—实践—认证”的学习系统，帮助学员<br/>获得真正说英语的自信。</p></div>'
          }
        ],
        cont2: [
          {
            title: '英语四六级学习资料',
            time: '2017-6-11',
            text: '<div><img src="../../static/img/art1.jpg" width="100%">英语四六级学习资料</div>'
          },
          {
            title: '少儿英语教材',
            time: '2017-7-11',
            text: '<div><img src="../../static/img/art1.jpg" width="100%">少儿英语教材</div>'
          },
          {
            title: '雅思新托福最新动态',
            time: '2017-8-11',
            text: '<div><img src="../../static/img/art1.jpg" width="100%">雅思新托福最新动态</div>'
          },
          {
            title: '最新专业八级资料',
            time: '2017-10-11',
            text: '<div><img src="../../static/img/art1.jpg" width="100%">最新专业八级资料</div>'
          }
        ],
        pic: '<div class="follow"><img src="../../static/img/follow.png" alt=""></div>'
      }
    },
    methods: {
      follow() {
        MessageBox({
          title: '',
          message: this.pic,
          confirmButtonText: '扫一扫，关注我们'
        })
      }
    }
  }
</script>

<template>
  <div id="menuColDiv" class="menu-col" :class="menuColClass">
    <!-- 文章类目框 -->
    <div class="article-catalog" v-show="menuColInnerShowSwitch==1" data-mcs-theme="light-thin">
      <!-- 搜索框 -->
      <div class="search-input-block">
        <div class="search-input-wrapper">
          <input type="text" class="search-input" placeholder=" Search..">
          <i class="search-input-icon"></i>
        </div>
      </div>

      <!-- 文章标签框 -->
      <div class="tag-block">
        <div class="tag-switch-wrapper">
          标 签 :
          <el-switch v-model="tagSearchSwitch" class="tag-switch"></el-switch>
        </div>
        <transition name="fade" v-on:enter="renderTag">
          <div class="tag-area" v-if="tagSearchSwitch" key="tagArea" data-mcs-theme="light-thin">
            <ATag class="a-tag">
              测试标签
            </ATag>
            <ATag class="a-tag">
              测试标签
            </ATag>
            <ATag class="a-tag">
              测试标签
            </ATag>
          </div>
        </transition>
      </div>

      <!-- 文章类目框 -->
      <div class="catalog-block">
        <ArticleBtn/>
      </div>

      <div class="bottom-line">------ 我也是有底线的! ------</div>
    </div>
    <!-- 个人简介 -->
    <AboutMe v-show="menuColInnerShowSwitch==2"/>
  </div>
</template>

<script>
  import AboutMe from '@/components/profile/AboutMe'
  import ATag from '@/components/toolkit/ATag'
  import ArticleBtn from '@/components/toolkit/ArticleBtn'

  export default {
    name: 'menuCol',
    data: function () {
      return {
        menuColInnerShowSwitch: this.showSwitch,// 菜单栏切换显示开关 1-文章类目 2-自我介绍
        searchText: "",//搜索字符串
        tagSearchSwitch: true,//标签框显示开关
      }
    },
    props: {
      showSwitch: {
        type: Number,
        required: true
      }
    },
    computed: {
      'menuColClass': function () {
        return {
          'enter': this.menuColInnerShowSwitch !== -1 && this.menuColInnerShowSwitch !== 0,
          'leave': this.menuColInnerShowSwitch === -1
        }
      }
    },
    watch: {
      'showSwitch': function (val) {
        this.menuColInnerShowSwitch = val;
      }
    },
    components: {
      'AboutMe': AboutMe,
      'ATag': ATag,
      'ArticleBtn': ArticleBtn
    },
    methods: {
      renderScrollBar: function () {
        $(".article-catalog").mCustomScrollbar();
        $(".tag-area").mCustomScrollbar();
      },
      renderTag: function () {
        //let fontSizeArr = ["12px", "20px", "16px"];
        //let fontSize = fontSizeArr[parseInt(Math.random() * 2)];
        //$(this).css("font-size", fontSize);
        let bgColorArr = ["rgba(128, 0, 0, .1)", "rgba(255, 0, 0, .1)", "rgba(0, 128, 0, .1)", "rgba(0, 255, 0, .1)", "rgba(0, 0, 128, .1)", "rgba(0, 0, 255, .1)"];
        $(".a-tag").each(function () {
          let bgColor = bgColorArr[parseInt(Math.random() * 5)];
          $(this).css("background-color", bgColor);
        });

        this.renderScrollBar();
      }
    },
    mounted: function () {
      this.renderScrollBar();
      this.renderTag();
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .menu-col {
    width: 380px;
    height: 100%;
    position: fixed;
    left: -100px;
    z-index: 499;
    display: none;
    padding: 10px;
  }

  .article-catalog {
    width: 100%;
    height: 100%;
  }

  .search-input {
    width: 320px;
    height: 100%;
    outline: none;
    -webkit-appearance: none;
    border-radius: 0;
    background-color: transparent;
    vertical-align: middle;
    color: #fff;
    font-size: 16px;
  }

  .search-input-wrapper {
    display: inline-block;
    width: 350px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    border-bottom: 2px solid #fff;
  }

  .search-input-block {
    text-align: center;
    height: 30px;
    margin-top: 10px;
  }

  .search-input-icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    vertical-align: middle;
    background-image: url("../../assets/icon-search.png");
    background-size: 20px 20px;
  }

  .search-input-icon:hover {
    cursor: pointer;
  }

  .tag-switch-wrapper {
    font-size: 14px;
    color: #fff;
    text-shadow: 1px 1px 1px #626464;
    height: 25px;
    line-height: 25px;
    padding: 10px;
  }

  .tag-switch {
    margin-bottom: 4px;
    margin-left: 5px;
  }

  .tag-area {
    width: 340px;
    height: 160px;
    background-color: rgba(255, 255, 255, .15);
    margin: 0 auto;
    padding: 10px;
  }

  .catalog-block {
    margin-top: 20px;
  }

  .bottom-line {
    text-align: center;
    font-size: 14px;
    color: #fff;
    text-shadow: 1px 1px 1px #626464;
    padding: 20px 0;
  }

  .enter {
    display: block;
    animation-name: leftEnterAnimate;
    animation-duration: .8s;
    animation-fill-mode: both;
    -webkit-animation-name: leftEnterAnimate;
    -webkit-animation-duration: .8s;
    -webkit-animation-fill-mode: both;
  }

  .leave {
    display: block;
    animation-name: leftLeaveAnimate;
    animation-duration: .8s;
    animation-fill-mode: both;
    -webkit-animation-name: leftLeaveAnimate;
    -webkit-animation-duration: .8s;
    -webkit-animation-fill-mode: both;
  }

  @keyframes leftEnterAnimate {
    0%, 60%, 75%, 90%, 100% {
      -webkit-animation-timing-function: cubic-bezier(.215, .61, .355, 1);
      animation-timing-function: cubic-bezier(.215, .61, .355, 1);
    }
    0% {
      -webkit-transform: translateZ(0);
      transform: translateZ(0);
    }
    60% {
      -webkit-transform: translate3d(425px, 0, 0);
      transform: translate3d(425px, 0, 0);
    }
    75% {
      -webkit-transform: translate3d(390px, 0, 0);
      transform: translate3d(390px, 0, 0);
    }
    90% {
      -webkit-transform: translate3d(405px, 0, 0);
      transform: translate3d(405px, 0, 0);
    }
    100% {
      -webkit-transform: translate3d(400px, 0, 0);
      transform: translate3d(400px, 0, 0);
    }
  }

  @keyframes leftLeaveAnimate {
    0%, 60%, 75%, 90%, 100% {
      -webkit-animation-timing-function: cubic-bezier(.215, .61, .355, 1);
      animation-timing-function: cubic-bezier(.215, .61, .355, 1);
    }
    0% {
      -webkit-transform: translate3d(433px, 0, 0);
      transform: translate3d(433px, 0, 0);
    }
    60% {
      -webkit-transform: translate3d(-25px, 0, 0);
      transform: translate3d(-25px, 0, 0);
    }
    75% {
      -webkit-transform: translate3d(10px, 0, 0);
      transform: translate3d(10px, 0, 0);
    }
    90% {
      -webkit-transform: translate3d(-5px, 0, 0);
      transform: translate3d(-5px, 0, 0);
    }
    100% {
      -webkit-transform: translateZ(0);
      transform: translateZ(0);
    }
  }

  :-moz-placeholder { /* Mozilla Firefox 4 to 18 */
    color: #fff;
    opacity: .9;
  }

  ::-moz-placeholder { /* Mozilla Firefox 19+ */
    color: #fff;
    opacity: .9;
  }

  input:-ms-input-placeholder {
    color: #fff;
    opacity: .9;
  }

  input::-webkit-input-placeholder {
    color: #fff;
    opacity: .9;
  }
</style>

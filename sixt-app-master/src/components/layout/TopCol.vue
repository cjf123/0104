<template>
  <div class="top-col">
    <!-- 顶部背景色 -->
    <div class="top-bg-block"></div>
    <!-- 顶部菜单按钮 -->
    <div class="top-menu-icon"></div>
    <!-- 顶部固定菜单栏 -->
    <div class="top-bar" :class="[topBarShadowClass,topBarOpacityClass]" v-show="topFixedBarSwitch">
      <ul v-show="topFixedBarTabSwitch">
        <li><a href="javascript:void(0)">主页</a></li>
        <li><a href="javascript:void(0)">菜单</a></li>
      </ul>
    </div>
    <!-- 头像区块 -->
    <div class="profile-pic-block">
      <ProfilePic class="profile-pic"/>
    </div>
    <!-- 简介区块 -->
    <div class="top-intro-Block">
      <!-- 昵称 -->
      <div class="profile-name-wrapper">
        <ProfileName class="profile-name" @showIntroBlock="showIntroBlock"/>
      </div>
      <!-- 描述 -->
      <div class="intro-text-wrapper">
        <QuoteText class="quote-text">
          <span>Don't worry , Be happy :-)</span>
        </QuoteText>
      </div>
      <!-- 联系方式 -->
      <div class="content-me-wrapper">
        <ContactMe class="contact-me"/>
      </div>
    </div>
  </div>
</template>

<script>
  import ProfilePic from '@/components/profile/ProfilePic'
  import ProfileName from '@/components/profile/ProfileName'
  import QuoteText from '@/components/toolkit/QuoteText'
  import NavBlock from '@/components/profile/NavBlock'
  import ContactMe from '@/components/profile/ContactMe'

  export default {
    name: 'topCol',
    data: function () {
      return {
        topFixedBarSwitch: false,// 固定顶栏显示开关
        topFixedBarTabSwitch: false,// 固定顶栏切换菜单显示开关
        topFixedBarShadowSwitch: false,// 固定顶栏阴影显示开关
        topFixedBarOpacitySwitch: false,// 固定顶栏半透明开关
      }
    },
    computed: {
      topBarShadowClass: function () {
        return {
          'top-bar-shadow-class': this.topFixedBarShadowSwitch
        }
      },
      topBarOpacityClass: function () {
        return {
          'top-bar-opacity-class': this.topFixedBarOpacitySwitch
        }
      }
    },
    components: {
      'ProfilePic': ProfilePic,
      'ProfileName': ProfileName,
      'QuoteText': QuoteText,
      'NavBlock': NavBlock,
      'ContactMe': ContactMe
    },
    methods: {
      showIntroBlock: function () {
        this.$emit('showIntroBlock');
      },
      showCatalogBlock: function () {
        this.$emit('showCatalogBlock');
      },
      topScroll: function () {
        let scrollTop = $(window).scrollTop();
        this.topFixedBarSwitch = scrollTop > 78;
        this.topFixedBarTabSwitch = scrollTop > 174;
        this.topFixedBarShadowSwitch = scrollTop > 291;
        this.topFixedBarOpacitySwitch = scrollTop > 332;
      }
    },
    mounted: function () {
      window.addEventListener('scroll', this.topScroll);
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .top-col {
    width: 100%;
    height: 332px;
    background-color: #fff;
    box-shadow: 0 3px 3px #3E4043;
  }

  .top-bg-block {
    width: 100%;
    height: 120px;
    background-color: #24292E;
    position: absolute;
    z-index: 1;
  }

  .top-bar {
    width: 100%;
    height: 40px;
    background-color: #24292E;
    position: fixed;
    z-index: 200;
    display: flex; /*Flex布局*/
    display: -webkit-flex; /* Safari */
    align-items: center; /*指定垂直居中*/
    justify-content: center;
    color: #fff;
    opacity: 1;
    transition: opacity 0.8s ease-in-out 0s;
  }

  .top-bar ul {
    display: inline-block;
    width: 36%;
    height: 20px;
    border-radius: 5px;
    border: 1px gray solid;
    list-style: none outside none;
  }

  .top-bar ul li {
    display: inline-block;
    float: left;
    text-align: center;
    width: 50%;
    height: 100%;
    line-height: 100%;
  }

  .top-bar ul li a {
    display: inline-block;
    width: 100%;
    height: 100%;
    color: white;
    font-size: .7rem;
  }

  .top-menu-icon {
    display: inline-block;
    width: 25px;
    height: 25px;
    background-image: url("../../assets/icon-menu.png");
    background-size: 25px 25px;
    margin: 7px 0 0 8px;
    position: fixed;
    z-index: 250;
  }

  .top-intro-Block {
    position: relative;
    text-align: center;
    z-index: 100;
  }

  .top-bar-shadow-class {
    box-shadow: 0 3px 3px #3E4043;
  }

  .top-bar-opacity-class {
    opacity: .98 !important;
    transition: opacity 2s;
  }

  .profile-pic-block {
    padding-top: 20px;
    text-align: center;
    position: relative;
    z-index: 300;
  }

  .profile-name-wrapper {
    display: inline-block;
  }

  .profile-name {
    margin-top: 10px;
  }

  .intro-text-wrapper {
    padding: 0 10px;
  }

  .quote-text {
    margin-top: 15px;
  }

  .content-me-wrapper {
    padding-bottom: 20px;
  }

  .contact-me {
    margin-top: 20px;
  }
</style>

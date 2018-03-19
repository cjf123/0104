<template>
  <div class="left-col fl">
    <!-- 顶部背景色 -->
    <div class="top-bg-block"></div>
    <!-- 简介区 -->
    <div class="intro-block">
      <!-- 头像 -->
      <ProfilePic/>
      <!-- 昵称 -->
      <ProfileName class="profile-name" @showIntroBlock="showIntroBlock"/>
      <!-- 简介 -->
      <QuoteText class="quote-text">
        <span>Don't worry , Be happy :-)</span>
      </QuoteText>
    </div>
    <!-- 导航区 -->
    <NavBlock @showIntroBlock="showIntroBlock" @showCatalogBlock="showCatalogBlock"/>
    <!-- 联系方式 -->
    <ContactMe class="contact-me"/>
  </div>
</template>

<script>
  import ProfilePic from '@/components/profile/ProfilePic'
  import ProfileName from '@/components/profile/ProfileName'
  import QuoteText from '@/components/toolkit/QuoteText'
  import NavBlock from '@/components/profile/NavBlock'
  import ContactMe from '@/components/profile/ContactMe'

  export default {
    name: 'leftCol',
    data: function () {
      return {}
    },
    methods: {
      showIntroBlock: function () {
        this.$emit('showIntroBlock');
      },
      showCatalogBlock: function () {
        this.$emit('showCatalogBlock');
      }
    },
    components: {
      'ProfilePic': ProfilePic,
      'ProfileName': ProfileName,
      'QuoteText': QuoteText,
      'NavBlock': NavBlock,
      'ContactMe': ContactMe
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .left-col {
    width: 300px;
    height: 100%;
    position: fixed;
    z-index: 500;
    background-color: #fff;
    box-shadow: 3px 0 5px #676767;
  }

  .top-bg-block {
    width: 300px;
    height: 180px;
    background-color: #24292E;
    position: absolute;
    z-index: -1;
  }

  .intro-block {
    width: 90%;
    height: 280px;
    margin: 112px auto 0;
    text-align: center;
  }

  .profile-name {
    margin-top: 20px;
  }

  .quote-text {
    margin-top: 20px;
  }

  .contact-me {
    margin-top: 20px;
  }
</style>

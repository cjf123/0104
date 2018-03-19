<template>
  <div id="app">
    <div class="container">
      <transition name="fade" v-on:enter="clientSwitch">
        <!-- 左边栏 -->
        <LeftCol v-if="!topColSwitch"
                 key="leftCol"
                 @showIntroBlock="showIntroBlock"
                 @showCatalogBlock="showCatalogBlock"/>
        <!-- 顶栏 -->
        <TopCol v-else
                key="topCol"
                @showIntroBlock="showIntroBlock"
                @showCatalogBlock="showCatalogBlock"/>
      </transition>
      <!-- 菜单栏 - PC -->
      <MenuCol :showSwitch="menuColShowSwitch"/>
      <!-- 菜单栏 - 移动端 -->
      <!-- todo -->
      <!--<MobileMenuCol :mobileShowSwitch="mobileMenuColShowSwitch"/>-->
      <!-- 主内容区 -->
      <div class="main-col-wrapper" @click="closeMenuCol">
        <MainCol v-if="!topColSwitch" :class="mainColClass" :mainColAnimateSwitch="menuColShowSwitch" />
      </div>
      <!-- 背景动画 -->
      <canvas id="canvas"></canvas>
    </div>
  </div>
</template>

<script>
  import LeftCol from '@/components/layout/LeftCol'
  import TopCol from '@/components/layout/TopCol'
  import MenuCol from '@/components/layout/MenuCol'
  import MainCol from '@/components/layout/MainCol'
  import MobileMenuCol from '@/components/layout/MobileMenuCol'

  export default {
    name: 'app',
    data: function () {
      return {
        topColSwitch: false,// 顶栏开关
        menuColShowSwitch: 0,//菜单栏显示开关 0-初始化 -1-不显示 1-显示文字类目 2-显示自我介绍
        mobileMenuColShowSwitch: 0,//移动客户端菜单栏显示开关 0-初始化 -1-不显示 1-显示文字类目 2-显示自我介绍
      }
    },
    computed: {
      mainColClass: function () {
        return {
          'main-col-cnt': !this.topColSwitch
        }
      }
    },
    components: {
      'LeftCol': LeftCol,
      'TopCol': TopCol,
      'MenuCol': MenuCol,
      'MainCol': MainCol,
      'MobileMenuCol': MobileMenuCol
    },
    methods: {
      // 浏览器窗口大小变化时调用
      windowResize: function () {
        this.topColSwitch = getClientWidth() < widthThreshold;
      },
      // 显示文章类目栏
      showCatalogBlock: function () {
        if (this.topColSwitch) {

        } else {
          this.menuColShowSwitch = this.menuColShowSwitch === 1 ? -1 : 1;
        }
      },
      // 显示个人简介
      showIntroBlock: function () {
        if (this.topColSwitch) {

        } else {
          this.menuColShowSwitch = this.menuColShowSwitch === 2 ? -1 : 2;
        }
      },
      // 关闭菜单栏
      closeMenuCol: function () {
        if (this.topColSwitch) {

        } else {
          this.menuColShowSwitch = this.menuColShowSwitch === 0 ? 0 : -1;
        }
      },
      // 客户端尺寸切换时调用
      clientSwitch: function () {
        this.menuColShowSwitch = 0;
      }
    },
    mounted: function () {
      this.topColSwitch = getClientWidth() < widthThreshold;
      window.addEventListener('resize', this.windowResize);
    }
  }
</script>

<style scoped>
  .container {
    overflow-x: hidden;
  }

  .main-col-cnt {
    position: absolute;
    left: 300px;
    min-height: 100%;
  }

</style>

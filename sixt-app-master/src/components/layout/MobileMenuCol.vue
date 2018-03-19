<template>
  <div id="menuColDiv" class="menu-col" :class="menuColClass">
    <div class="article-catalog" v-show="menuColInnerShowSwitch==1">
      文章菜单
    </div>
    <div class="about-me" v-show="menuColInnerShowSwitch==2">
      关于我
    </div>
  </div>
</template>

<script>
  export default {
    name: 'mobileMenuCol',
    data: function () {
      return {
        menuColInnerShowSwitch: this.showSwitch,// 菜单栏切换显示开关 1-文章类目 2-自我介绍
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
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .menu-col {
    width: 400px;
    height: 100%;
    background-color: #00cbfc;
    position: fixed;
    left:-100px;
    z-index: 499;
    display: none;
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
</style>

<template>
  <div class="main-col" :class="mainColAnimateClass">
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'mainCol',
    data: function () {
      return {
        mainColInnerAnimateSwitch: this.mainColAnimateSwitch,// 主内容区动画切换开关
      }
    },
    props: {
      'mainColAnimateSwitch': {
        type: Number,
        required: true
      }
    },
    computed: {
      'mainColAnimateClass': function () {
        return {
          'enter': this.mainColInnerAnimateSwitch !== -1 && this.mainColInnerAnimateSwitch !== 0,
          'leave': this.mainColInnerAnimateSwitch === -1
        }
      }
    },
    methods: {},
    watch: {
      'mainColAnimateSwitch': function (val) {
        this.mainColInnerAnimateSwitch = val;
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .main-col {
    width:auto;
    min-height: 100%;
    background-color: #EAEAEA;
    padding: 10px 30px;
  }

  .enter {
    animation-name: leftEnterAnimate;
    animation-duration: 0.8s;
    animation-fill-mode: both;
    -webkit-animation-duration: .8s;
    -webkit-animation-fill-mode: both;
    -webkit-animation-name: leftEnterAnimate;
    background: none;
    transition: all .5s ease-in-out 0s;
  }

  .leave {
    animation-name: leftLeaveAnimate;
    animation-duration: .8s;
    animation-fill-mode: both;
    -webkit-animation-name: leftLeaveAnimate;
    -webkit-animation-duration: .8s;
    -webkit-animation-fill-mode: both;
    transition: all 1s ease-in-out 0s;
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
      -webkit-transform: translate3d(395px, 0, 0);
      transform: translate3d(395px, 0, 0);
    }
    75% {
      -webkit-transform: translate3d(360px, 0, 0);
      transform: translate3d(360px, 0, 0);
    }
    90% {
      -webkit-transform: translate3d(375px, 0, 0);
      transform: translate3d(375px, 0, 0);
    }
    100% {
      -webkit-transform: translate3d(370px, 0, 0);
      transform: translate3d(370px, 0, 0);
    }
  }

  @keyframes leftLeaveAnimate {
    0%, 60%, 75%, 90%, 100% {
      -webkit-animation-timing-function: cubic-bezier(.215, .61, .355, 1);
      animation-timing-function: cubic-bezier(.215, .61, .355, 1);
    }
    0% {
      -webkit-transform: translate3d(413px, 0, 0);
      transform: translate3d(413px, 0, 0);
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

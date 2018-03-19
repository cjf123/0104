<template>
  <div>
    <el-dialog
      title="打赏" :visible.sync="dialogVisibleSwitch" :append-to-body="true" :width="dialogWidth" top="8vh"
      @close="dialogClose">
      <transition name="fade" mode="out-in">
        <div class="question-block" v-if="!payImgSwitch" key="questionBlock">
          <p class="question-title">为什么需要打赏?</p>
          <p class="question-answer">1. 小站由本人自费运营 , 费用涉及 : 购买 域名/域名解析/云虚机/云RDS/云安全等服务.</p>
          <p class="question-answer">2. 小站坚持原创 , 希望能为您提供优质的内容 , 更希望得到您的鼓励和认可.</p>
          <p class="question-answer">3. 打赏是您的自愿行为 , 并非牟取利益的手段.</p>
          <p class="question-tip">-- 理解万岁 :-)</p>
          <p class="question-btn">
            <el-button type="primary" size="medium" @click="payImgSwitch = true">知道了</el-button>
          </p>
        </div>

        <div class="pay-img-block" v-else key="payImgBlock">
          <el-tabs type="border-card" value="alipay">
            <el-tab-pane label="支付宝" name="alipay">
              <div class="pay-img-wrapper">
                <img src="../../assets/pay-alipay.png" class="pay-img"/>
              </div>
            </el-tab-pane>
            <el-tab-pane label="微 信" name="wechat">
              <div class="pay-img-wrapper">
                <img src="../../assets/pay-wechat.png" class="pay-img"/>
              </div>
            </el-tab-pane>
            <el-tab-pane label="扫码领红包" name="alipayRedBag">
              <div class="pay-img-wrapper">
                <img src="../../assets/pay-alipay-redbag.png" class="pay-img"/>
              </div>
            </el-tab-pane>
          </el-tabs>
          <a class="question-link" href="javascript:void(0)" @click="payImgSwitch = false"><- 为什么需要打赏?</a>
        </div>
      </transition>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: 'donateDialog',
    data: function () {
      return {
        dialogVisibleSwitch: this.dialogVisible,
        payImgSwitch: false,// 支付图片展示开关
      }
    },
    computed: {
      dialogWidth: function () {
        let clientWidth = getClientWidth();
        if (clientWidth >= 700) {
          // 设备宽度大于700px , 则显示500px宽度
          return "400px";
        }
        if (clientWidth >= 400) {
          // 设备宽度大于400px , 则显示300px宽度
          return "300px";
        }
        // 设备宽度小于300px , 则显示90%屏幕宽度
        return "90%";
      }
    },
    props: {
      'dialogVisible': {
        type: Boolean,
        required: true
      }
    },
    methods: {
      dialogClose: function () {
        this.$emit('dialogClose');
      }
    },
    watch: {
      dialogVisible: function (val) {
        this.dialogVisibleSwitch = val;
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .question-title {
    font-size: 18px;
    font-weight: 800;
  }

  .pay-img {
    display: inline-block;
    width: 200px;
    height: 200px;
    background-size: 200px;
  }

  .pay-img-block {
    margin-top: -25px;
  }

  .pay-img-wrapper {
    text-align: center;
  }

  .question-btn {
    margin-top: 10px;
    text-align: center;
  }

  .question-answer {
    color: #676767;
    padding-top: 5px;
  }

  .question-tip {
    color: #25B887;
    padding-top: 5px;
  }

  .question-link {
    color: #3D9DFA;
    font-size: 14px;
  }

  .question-link:hover {
    color: #5DAAF7;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s
  }

  .fade-enter, .fade-leave-to {
    opacity: 0
  }
</style>

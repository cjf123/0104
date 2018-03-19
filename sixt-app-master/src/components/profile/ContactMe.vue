<template>
  <div class="contact-block">
    <div class="contact-wrapper">
      <ul>
        <li>
          <a href="https://github.com/pertrichor" title="Github : https://github.com/pertrichor" target="_blank"
             class="icon-github contact-icon"></a>
        </li>
        <li>
          <a href="mailto:pertrichor@163.com" title="Email : pertrichor@163.com" class="icon-email contact-icon"></a>
        </li>
        <!--<li>-->
        <!--<a href="javascript:void(0)" @click="dialogVisibleSwitch = true" class="icon-donate contact-icon"></a>-->
        <!--</li>-->
      </ul>
      <div class="clearfix"></div>
    </div>
    <DonateDialog :dialogVisible="dialogVisibleSwitch" @dialogClose="dialogClose"/>
  </div>
</template>

<script>
  import DonateDialog from '@/components/toolkit/DonateDialog'

  export default {
    name: 'contactMe',
    data: function () {
      return {
        dialogVisibleSwitch: false,//控制打赏弹框展示
        isMobile: this.isMobileFlag
      }
    },
    components: {
      'DonateDialog': DonateDialog
    },
    methods: {
      dialogClose: function () {
        this.dialogVisibleSwitch = false;
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .contact-block {
    text-align: center;
  }

  .contact-wrapper {
    display: inline-block;
    margin: 0 auto;
  }

  .contact-block ul li {
    float: left;
    padding: 2px 8px;
  }

  .contact-block ul li a {
    display: inline-block;
    width: 25px;
    height: 25px;
  }

  .icon-github {
    background-image: url("../../assets/icon-github.png");
  }

  .icon-email {
    background-image: url("../../assets/icon-email.png");
  }

  .icon-donate {
    background-image: url("../../assets/icon-donate.png");
  }

  .contact-icon {
    background-size: 25px 25px;
    opacity: .6;
  }

  .contact-icon:hover {
    opacity: .9;
  }
</style>

<template>
  <div class="our">
    <div class="form-title">
      <span class="back-home mintui mintui-back" @click="back">返回</span>
      <span>申请试听</span>
    </div>

    <mt-field label="用户名" placeholder="请输入姓名" v-model="username"></mt-field>
    <mt-field label="密码" placeholder="请输入密码" type="password" v-model="password"></mt-field>
    <mt-field label="邮箱" placeholder="请输入邮箱" type="email" v-model="email"></mt-field>
    <mt-field label="手机号" placeholder="请输入手机号" type="tel" v-model="phone"></mt-field>
    <mt-radio
      title="请选择试听课程"
      v-model="course"
      :options="['幼儿英语', '青少儿英语', '中学英语','高中英语','雅思新托福','口译口语','英语四六级','专业四八级']">
    </mt-radio>
    <div class="submit">
      <mt-button @click="sub" type="danger">提交</mt-button>
    </div>

  </div>
</template>
<script>
  import '../../static/css/foot.css'
  import {MessageBox} from 'mint-ui';

  export default {
    data() {
      return {
        username: '',
        phone: '',
        password:'',
        email:'',
        course: '',
        arry: []
      }
    },
    methods: {
      back() {
        this.$router.go(-1)
      },
      sub() {
        if (this.username && this.phone && this.password && this.course && this.email) {
          this.arry.unshift({username: this.username, phone: this.phone, password: this.password, course: this.course,email:this.email})
          MessageBox.alert('课程申请成功！').then(action => {
            this.$router.push('/home')
          });
        } else {
          MessageBox.alert('请输入正确信息！')
        }

      }
    }
  }
</script>
<style>
  .our {
    text-align: left
  }
</style>

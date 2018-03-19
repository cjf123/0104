import Vue from 'vue'
import Router from 'vue-router'
import Home from '../pages/home'
import About from '../pages/about'
import Course from '../pages/course'
import school from '../pages/school'
import Our from '../pages/our'
import Teacher from '../pages/teacher'
import From from '../pages/From'
import News from '../pages/News'
import News1 from '../pages/News1'
import Introduce from '../pages/introduce'
import Youer from '../pages/home/Youer'
import Shaoer from '../pages/home/Shaoer'
import Zhongxue from '../pages/home/Zhongxue'
import HightSchool from '../pages/home/HightSchool'
import Yasi from '../pages/home/Yasi'
import Oral from '../pages/home/Oral'
import CET from '../pages/home/CET'
import TEM from '../pages/home/TEM'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/home',
      component: Home
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/course',
      component: Course
    },
    {
      path: '/school',
      component: school
    },
    {
      path: '/our',
      component: Our
    },
    {
      path: '/teacher',
      component: Teacher
    },
    {
      path: '/from',
      component: From
    },
    {
      name:'News',
      path: '/News',
      component: News
    },
    {
      name:'News1',
      path: '/News1',
      component: News1
    },
    {
      path: '/introduce',
      component: Introduce
    },
    {
      path: '/Youer',
      component: Youer
    },
    {
      path: '/Shaoer',
      component: Shaoer
    },
    {
      path: '/Zhongxue',
      component: Zhongxue
    },
    {
      path: '/HightSchool',
      component: HightSchool
    },
    {
      path: '/Yasi',
      component: Yasi
    },
    {
      path: '/Oral',
      component: Oral
    },
    {
      path: '/CET',
      component: CET
    },
    {
      path: '/TEM',
      component: TEM
    }
  ]
})

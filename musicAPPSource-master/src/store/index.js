import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
// 这种写法师一种简写的方式，不然要以{}的方式书写，而这种方式就是可以通过getters.xxx去访问
import * as getters from './getters'
import state from './state'
import mutations from './mutations'
// 这个是个查看vuex修改的日志，当我们通过mutations修改state的时候，他会打印出state之前的状态和之后的状态
import createLogger from 'vuex/dist/logger'

Vue.use(Vuex)
// 这个是一个判断是否是测试环境，如果是测试环境的话就开启vuex的debug模式
// 这个模式会判断vuex是否是通过mutation去修改state的值的
const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  actions,
  getters,
  state,
  mutations,
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
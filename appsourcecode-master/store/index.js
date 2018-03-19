import Vue from 'vue'
import vuex from 'vuex'
import data from '../components/data.js'
Vue.use(vuex)

export default new vuex.Store({
  modules:{
    mData:data
  }
})

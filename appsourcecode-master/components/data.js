export default ({
  state:{
    aaa:'111'
  },
  mutations:{
    add(state){
      state.aaa+='test'
    }
  },
  action:{
    add2(state){
      if(1<0){
        state.commit('add')
      }
    }
  },
  getters:{
    add3(state){
      return state.aaa+'ccc'
    }
  }
})

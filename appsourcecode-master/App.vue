<template>
  <div id="app">
    <HeadTop></HeadTop>
    <transition :name="animate">
      <router-view class="content" keep-alive></router-view>
    </transition>
    <FootEnd></FootEnd>
  </div>
</template>

<script>
  import '../static/css/app.css'
  import '../static/css/rest.css'
  import HeadTop from './components/HeadTop'
  import FootEnd from './components/Foot'

  export default {
    components: {HeadTop, FootEnd},
    data(){
    	return{
    		animate:"animate"
    	}
    },
    watch:{
    	$route(to,from){
    		if(from.path=="/News" || from.path=="/News1" || from.path=="/From"){
    			this.animate="animate2"
    		}else{
    			this.animate="animate"
    		}
    	}
    }
  }
</script>

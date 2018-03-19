<template>
  <div class="news">
    <h3 class="news-title">
      {{this.$route.params.cont2[getIndex].title}}
    </h3>
    <span class="news-time">
      发布时间：{{$route.params.cont2[getIndex].time}}
    </span>
    <p class="news-content" v-html="content"></p>

    <div class="page-news page-top" @click="last" v-if="getIndex>0">上一个新闻：<span>{{this.$route.params.cont2[getIndex - 1].title}}</span>
    </div>
    <div class="page-top" v-else>上一个新闻：没有了</div>
    <div class="page-news page-bottom" @click="next" v-if="getIndex<this.$route.params.cont2.length-1">
      下一个新闻：<span>{{this.$route.params.cont2[getIndex + 1].title}}</span>
    </div>
    <div class="page-bottom" v-else>下一个新闻：没有了</div>
    <div class="back" @click="back">
      返回
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        getIndex: this.$route.params.index2,
        content: this.$route.params.cont2[this.$route.params.index2].text
      }
    },
    methods: {
      back() {
        this.$router.go(-1)
      },
      last() {
        if (this.getIndex > 0) {
          this.getIndex--
          this.content = this.$route.params.cont2[this.getIndex].text
        }
      },
      next() {
        if (this.getIndex < this.$route.params.cont2.length - 1) {
          this.getIndex++
          this.content = this.$route.params.cont2[this.getIndex].text
        }
      }
    }
  }
</script>

<template>
  <div class="main-cnt">

    <ArticleBlock/>
    <ArticleBlock/>
    <ArticleBlock/>
  </div>
</template>

<script>
  import ArticleBlock from '@/components/article/ArticleBlock'

  export default {
    name: 'mainIndex',
    data: function () {
      return {}
    },
    methods: {},
    components: {
      'ArticleBlock': ArticleBlock
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

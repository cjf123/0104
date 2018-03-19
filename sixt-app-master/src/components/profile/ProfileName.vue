<template>
  <div>
    <a class="profile-name" href="javascript:void(0)" @click="nameClick">Blue</a>
  </div>
</template>

<script>
  export default {
    name: 'profileName',
    data: function () {
      return {}
    },
    methods: {
      'nameClick': function () {
        window.location.href=domain;
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .profile-name {
    color: #4D4D4D;
    font-size: 30px;
    font-weight: 600;
  }

  .profile-name:hover {
    color: #25B887;
  }
</style>

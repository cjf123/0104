<template>
  <div class="profile-pic"></div>
</template>

<script>
  export default {
    name: 'profilePic',
    data: function () {
      return {}
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .profile-pic {
    display: inline-block;
    width: 128px;
    height: 128px;
    border: 5px solid #ffffff;
    border-radius: 128px;
    background-image: url("../../assets/profile-pic.png");
  }
</style>

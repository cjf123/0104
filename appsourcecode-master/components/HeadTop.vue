<template>
  <div>
    <ul id="nav">
      <li>
        <router-link :to="{path:'/home'}">
          <img src="../assets/images_home/nav_home_normal_05.png">
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/course'}">课程</router-link>
      </li>
      <li>
        <router-link :to="{path:'/teacher'}">师资</router-link>
      </li>
      <li>
        <router-link :to="{path:'/school'}">校区</router-link>
      </li>
      <li>
        <router-link :to="{path:'/our'}">学员</router-link>
      </li>
      <li>
        <router-link :to="{path:'/about'}">我们</router-link>
      </li>
    </ul>
  </div>

</template>
<script>
  import '../../static/css/head.css'
</script>

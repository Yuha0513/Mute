<template>
  <div class="home_user_box">
    <p class="user_hello"> 안녕하세요 {{ userInfo?.username }} 님</p>
    <img :src="userprofile" class="user_profile">
  </div>
</template>

<script>
export default {
    name:'HomeUser',
    computed: {
        userInfo() {
            return this.$store.state.user
        },
        userprofile() {
            return this.$store.state.userDetail.selfimg
        }
    }
}
</script>

<style>
.home_user_box{
    height: 170px;
    margin-top: 90px;
    
}
.user_profile {
    margin-top: 10px;
    width: 100px;
  
}
.user_hello {
    width: 180px;
}
</style>
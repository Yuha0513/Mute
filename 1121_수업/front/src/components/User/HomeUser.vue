<template>
  <div class="home_user_box">
    안녕하세요
    {{ userInfo.username }} 님
    <img :src="userprofile" width="100px">
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

    margin-top: 50px;
}
</style>
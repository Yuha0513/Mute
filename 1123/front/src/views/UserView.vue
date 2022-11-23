<template>
  <div>
    <div class="user_container">
      <div class="avatar-flip">
        <img :src="userimg1" height="150" width="150">
        <img :src="userimg2" height="150" width="150">
      </div>
      <h2>{{ userInfo.username }}</h2>
      <button v-if="is_followed === false" @click="followFunc">follow</button>
      <button v-if="is_followed === true" @click="followFunc">unfollow</button>
      <hr>
      <h3 class="user_h3">자기소개</h3>
      <p id="usercontent">{{ userDetail.selfintroduce }}</p>
      <hr>
      <h3 class="user_h3">좋아하는 영화</h3>
      <p id="usercontent">
        <LikeList/>
      </p>
      <router-link :to="{ name: 'userupdate' }"><button>정보 수정</button></router-link>
      <router-link :to="{ name: 'password' }"><button>비밀번호 변경</button></router-link>
    </div>
  </div>
  
</template>

<script>
import LikeList from '@/components/LikeList'

export default {
    name: 'UserView',
    // methods: {
    //   getUser() {
    //     this.$store.dispatch('getUser')
    //   }
    // },
    computed: {
      userInfo() {
        return this.$store.state.user
      },
      is_followed() {
        return this.$store.state.is_followed
      },
      userDetail() {
        return this.$store.state.userDetail
      },
      userimg1 () {
        return this.$store.state.userDetail.selfimg
      },
      userimg2 () {
        return this.$store.state.userDetail.otherimg
      },

    },
    created() {
      this.$store.dispatch('getUser')
 
    },
    methods: {
      followFunc() {
        this.$store.dispatch('followUser')

      },
      getUserPic() {
        this.$store.dispatch('getUserPic')
      }
    },
    components: {
      LikeList
    },

}
</script>

<style>
.user_container {
  width: 400px;
  margin: 120px auto 120px;
  background-color: #fff;
  padding: 0 20px 20px;
  border-radius: 6px;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  box-shadow: 0 3px 6px rgba(0,0,0,0.075);
  -webkit-box-shadow: 0 3px 6px rgba(0,0,0,0.075);
  -moz-box-shadow: 0 3px 6px rgba(0,0,0,0.075);
  text-align: center;
}
.user_container:hover .avatar-flip {
  transform: rotateY(180deg);
  -webkit-transform: rotateY(180deg);
}
.user_container:hover .avatar-flip img:first-child {
  opacity: 0;
}
.user_container:hover .avatar-flip img:last-child {
  opacity: 1;
}
.avatar-flip {
  border-radius: 100px;
  overflow: hidden;
  height: 150px;
  width: 150px;
  position: relative;
  margin: auto;
  top: -60px;
  transition: all 0.3s ease-in-out;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  box-shadow: 0 0 0 13px #f0f0f0;
  -webkit-box-shadow: 0 0 0 13px #f0f0f0;
  -moz-box-shadow: 0 0 0 13px #f0f0f0;
}
.avatar-flip img {
  position: absolute;
  left: 0;
  top: 0;
  border-radius: 100px;
  transition: all 0.3s ease-in-out;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
}
.avatar-flip img:first-child {
  z-index: 1;
}
.avatar-flip img:last-child {
  z-index: 0;
  transform: rotateY(180deg);
  -webkit-transform: rotateY(180deg);
  opacity: 0;
}
h2 {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 15px;
  color: #333;
}
.user_h3 {
  font-size: 16px;
  color: #00baff;
  letter-spacing: 1px;
  margin-bottom: 25px
}
#usercontent {
  font-size: 16px;
  line-height: 26px;
  margin-bottom: 20px;
  color: #666;
}
</style>
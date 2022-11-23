<template>
   <div>
    <div class="user_container">
      <div class="avatar-flip">
        <img :src="otherimg" height="150" width="150">
        <!-- <img :src="userimg2" height="150" width="150"> -->
      </div>
      <h2>{{ otherinfo.username }}</h2>
      <button v-if="isfollow === false"  @click="followUser">follow</button>
      <button v-if="isfollow === true" @click="followUser">unfollow</button>
      <hr>
      <h3 class="user_h3">자기소개</h3>
      <p id="usercontent"></p>
      <hr>
      <h3 class="user_h3">좋아하는 영화</h3>
      <p id="usercontent">
      </p>
      {{ like }}
    </div>
  </div>

</template>

<script>


export default {
    name: 'OtherProfile',
    data() {
      return {
        like: []
      }
    },
    methods: {
        getOtherInfo() {
            this.$store.dispatch('getOtherInfo')
        },
        // likemovieFinder() {
        //   console.log('작동')
        //   this.otherinfo.likemovies.forEach(likemovie => {
        //     console.log(likemovie)
        //     this.$store.state.movies.forEach(movie => {
        //       console.log(movie)
        //       if(likemovie === movie.id) {
        //         let likes = {
        //           movie: this.movie
        //         }
        //         this.like = likes
        //       }
        //     });
        //   });
        // },
        followUser() {
          this.$store.dispatch('followUser')
          this.$store.dispatch('checkfollower')
        }
    },
    computed: {
      otherinfo() {
        return this.$store.state.otherInfo
      },
      otherimg() {
        return this.$store.state.otherInfo.image
      },
      isfollow() {
        return this.$store.state.is_followed
      }

    },
    created() {
      this.likemovieFinder()
    }
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
<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarNavAltMarkup">
            <ul class="navbar-nav">
              <li><router-link class="nav-link active" :to="{ name: 'home' }">home</router-link></li>
              <li><router-link class="nav-link active" :to="{ name: 'movies' }">movie</router-link></li>
              <li><router-link class="nav-link active" :to="{ name: 'trip' }">trip</router-link></li>
            </ul>
            <ul class="navbar-nav">
              <li><router-link class="nav-link" :to="{ name: 'signup' }" v-if="isLogin === false">회원가입</router-link></li>
              <li><router-link class="nav-link" :to="{ name: 'login' }" v-if="isLogin === false">login</router-link></li>
              <li @click="logout" class="nav-link" v-if="isLogin === true">logout</li>
              <router-link :to="{ name: 'user' }" v-if="isLogin === true" ><i class="nav-link fa-sharp fa-solid fa-user"></i></router-link>
            </ul>
        </div>
      </div>
    </nav>
    <router-view/>
    <SwiperMovie/>
  </div>
</template>

<script>
import SwiperMovie from '@/components/Movie/SwiperMovie'
  export default {
    methods: {
      logout() {
        this.$store.dispatch('logout')
      },
      goHome() {
        this.$router.push({ name: 'home'})
      },
    
    },
    computed: {
      isLogin() {
        return this.$store.state.isLogined // 로그인 버젼 구현 아직 2022.11.16
      }
    },
    components: {
      SwiperMovie
    }
  }
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.nav-link {
  margin-left: 10px;
  margin-right: 10px;
  border-radius: 10px;
}
.navbar-brand {
  margin-right: 70px;
}
.nav-link:hover{
  background-color: #cad1cf;
  

}
ul {
  list-style:none;
}

</style>

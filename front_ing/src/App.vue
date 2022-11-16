<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'movies' }">movie</router-link> |
      <router-link :to="{ name: 'trip' }">trip</router-link> |
      <router-link :to="{ name: 'user' }">user</router-link>  |
      <router-link v-if="isLogin === false" :to="{ name: 'signup' }">회원가입</router-link>  |
      <router-link v-if="isLogin === false" :to="{ name: 'login'}">LOGIN</router-link>  |
      <button v-if="isLogin === true" @click="logout">logout</button>
    </nav>
    <router-view/>
  </div>
</template>
<script>
  export default {
    methods: {
      logout() {
        this.$store.dispatch('logout')
      } 
    },
    computed: {
      isLogin() {
        return this.$store.state.isLogined // 로그인 버젼 구현 아직 2022.11.16
      }
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<template>
  <div id="app">
    <!-- <nav>
      <router-link :to="{ name: 'movies' }">movie</router-link> |
      <router-link :to="{ name: 'trip' }">trip</router-link> |
      <router-link :to="{ name: 'user' }">user</router-link>  |
      <router-link :to="{ name: 'signup' }">회원가입</router-link>  |
      <router-link :to="{ name: 'login'}">LOGIN</router-link>  |
      <button @click="logout">logout</button>
    </nav> -->

    <nav class="navbar">
        <div class="navbar__logo">
            <i class="fab fa-accusoft"></i>
            <a href="">Logo</a>
        </div>

        <ul class="navbar__menu">
            <li><router-link :to="{ name: 'movies' }">movie</router-link></li>
            <li><router-link :to="{ name: 'trip' }">trip</router-link></li>
            <li><router-link :to="{ name: 'user' }">user</router-link></li>
            <li><router-link :to="{ name: 'signup' }">회원가입</router-link></li>
            <li><button @click="logout">logout</button></li>
        </ul>

        <ul class="navbar__icons">
            <li><i class="fab fa-twitter"></i></li>
            <li><i class="fab fa-facebook-f"></i></li>
        </ul>

        <a href="#" class="navbar__toogleBtn">
            <i class="fas fa-bars"></i>
        </a>
    </nav>
    <router-view/>
    <!-- <testView/> -->
  </div>
</template>

<script>
// import testView from '@/components/testView'
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
    },
    components: {
      // testView
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

:root{
    --text-color: #f0f4f5;
    --background-color: #263343;
    --accent-color:#d49466;
}

body {
    margin: 0px;
    font-family: 'Open sans';
}

a {
    text-decoration: none;
    color: white;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background:#263343;
    padding: 8px 12px;
}

.navbar__logo {
    font-size: 24px;
    color: white;
}

.navbar__logo i {
    color: #d49466;
}

.navbar__menu {
    display: flex;
    list-style: none;
    padding-left: 0px;
}

.navbar__menu li {
    padding: 8px 12px;

}

.navbar__menu :hover {
    background: #d49466;
    border-radius: 4px;
}

.navbar__icons {
    list-style: none;
    color: white;
    display: flex;
    padding-left: 0px;
}

.navbar__icons li {
    padding: 8px 12px;
}

.navbar__toogleBtn {
    display: none;
    position: absolute;
    right: 32px;
    font-size: 24px;
    color: #d49466;
}
</style>

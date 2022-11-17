<template>
    <div class="container">
        <div class="main">
            <h3 class="logo">Login</h3>
            <form @submit.prevent class="container">
                <input type="text" id="username" v-model="username" class="account" placeholder="아이디">                
                <input type="password" id="password" v-model="password" class="account" placeholder="비밀번호">
                <input type="submit" class='account' id="login" value="logIn" @click="logIn ">
                <p class="suggest">Don't Have an Account? <router-link :to="{ name: 'signup'}">signup</router-link></p>
            </form>


        </div>
    </div>
</template>

<script>

export default {
    name: 'LoginView',
    data() {
        return {
            username: null,
            password: null,
        }
    },
    methods: {
        logIn() {
            const username = this.username
            const password = this.password

            const payload = {
                username: username,
                password: password,
            }
            this.$store.dispatch('logIn', payload)
        }
    }
}
</script>

<style>
.container{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.main {
    margin-top: 30px;
    width: 350px;
    height: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border: 1px solid lightgrey;
    border-radius: 5px;
}

.logo {
    margin-top: 0px;
    margin-bottom: 40px;
}

#login {
    width: 100%;
    background-color: rgb(93, 216, 169);
    border-color: transparent;
    color: white;
    margin-top: 20px;
}

.account {
    display: block;
    margin-bottom: 3px;
    padding: 3px;
    border: 1px solid lightgray;
    border-radius: 3px;
    margin-bottom: 10px;
}
.suggest {
    color: gray;
    font-size: small;
}
</style>
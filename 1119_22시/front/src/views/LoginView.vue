<template>
    <div class="login_container">
        <div class="login_main">
            <h3 class="login_logo">Login</h3>
            <form @submit.prevent class="form_container">
                <input type="text" id="username" v-model="username" class="account" placeholder="아이디">                
                <input type="password" id="password" v-model="password" class="account" placeholder="비밀번호">
                <input type="submit" class='account' id="login" value="logIn" @click="logIn ">
                <p class="suggest">Don't Have an Account? <router-link :to="{ name: 'signup'}" class="suggets_link">signup</router-link></p>
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
            this.$store.dispatch('getgetUser')
        }
    }
}
</script>

<style>
.login_container{
    
    display: flex;
    flex-direction: column;
    align-items: center;
}
.login_main {
    margin-top: 30px;
    width: 350px;
    height: 350px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border: 1px solid lightgrey;
    border-radius: 5px;
   
}

.login_logo {
    margin-top: 0px;
    height: 10px;
}

#login {
    width: 200px;
    background-color: rgb(93, 216, 169);
    border-color: transparent;
    color: white;
    
}

.account {
    width: 190px;
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
.form_container {
    margin-top: 20px;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.suggets_link {
    color: rgb(81, 180, 142);
}
</style>
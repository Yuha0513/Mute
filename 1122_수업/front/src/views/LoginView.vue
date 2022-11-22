<template>
    <div class="login_container">
        <div class="login-box">
            <p class="login_logo">Login</p>
            <form @submit.prevent class="login_form">
                <input type="text" id="username" v-model="username" class="login_form input" placeholder="아이디">                
                <input type="password" id="password" v-model="password" class="login_form input" placeholder="비밀번호">
                <input type="submit" class='login_input' id="login" value="logIn" @click="logIn ">
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
    margin-top: 70px;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.login-box {

width: 400px;
height: 320px;
border-radius: 3px;
margin: auto;
border-radius: 3px;
background-color: white;
box-shadow: 3px 3px 3px 3px gray;
}

.login_logo {
    color: #49c1a2;
    margin-top: 30px;
    margin-bottom: 20px;
    height: 10px;
    font-size: large;
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
    margin-top: 5px;
}
.suggets_link {
    color: rgb(81, 180, 142);
}
.login_form {
  width: 300px;
  margin-left: 27px;
}
.login_form input {
  width: 100%;
  padding: 7px;
  border: none;
  border: 1px solid gray;
  border-radius: 6px;
  outline: none;
  margin-top: 20px;
}
.login_input {
    margin-left: 27px;
    width: 320px;
    height: 35px;
    margin-top: 20px;
    border: none;
    background-color: #49c1a2;
    color: white;
    font-size: 18px;
}
</style>
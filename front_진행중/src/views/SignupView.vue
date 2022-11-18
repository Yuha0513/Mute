<template>
    <div class="container">
        <div class="signupzone">
            <h2>회원가입</h2>
            <form @submit.prevent="signUp">
            <label for="username">아이디 : </label>
            <input type="text" id="username" v-model="username"> <br>

            <label for="password1">비밀번호 : </label>
            <input type="password" id="password1" v-model="password1"> <br>

            <label for="password2">비밀번호 확인 : </label>
            <input type="password" id="password2" v-model="password2"> <br>

            <input type="submit" value="SignUp">
        </form>
        </div>
        <div class="adzone">
        </div>
    </div>
</template>

<script>
export default {
    name: 'SignupView',
    data() {
        return {
            username: null,
            password1: null,
            password2: null,
        }
    },
    methods: {
        signUp() {
            const username = this.username
            const password1 = this.password1
            const password2 = this.password2

            const payload = {
                username: username,
                password1: password1,
                password2: password2,
            }

            this.$store.dispatch('signUp', payload)
        }
    }

}
</script>

<style>
.container {
    margin-top: 70px;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    
}
.signupzone {
    width: 500px;
    height: 700px;
    border: solid 1px gray;
    border-radius: 3px;
    margin-right: 10px;
    box-shadow: 3px 3px 3px 3px gray;
}
/* .adzone {
    width: 500px;
    height: 700px;
    border: solid 1px gray;
    border-radius: 3px;
    margin-left: 10px;
} */
</style>
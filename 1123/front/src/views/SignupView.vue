<template>
    <div class="sign_container">
        <div class="signupzone">
            <p class="signup_h2">회원가입</p>
            <form @submit.prevent="signUp" class="sign_form">
                <label for="username" class="sign_form label">아이디 : </label>
                <input type="text" id="username" v-model="username" class="sign_form input"> <br>

                <label for="password1" class="sign_form label">비밀번호 : </label>
                <input type="password" id="password1" v-model="password1" class="sign_form input"> <br>

                <label for="password2" class="sign_form label">비밀번호 확인 : </label>
                <input type="password" id="password2" v-model="password2" class="sign_form input"> <br>

                <input type="submit" value="SignUp" class="sign_input">
            </form>
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
.sign_container {
    display: flex;
    margin-top: 70px;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    
}
.signupzone {
  width: 400px;
  height: 620px;
  margin: auto;
  background-color: white;
  border-radius: 3px;
  align-content: center;
  text-align: center;
  box-shadow: 3px 3px 3px 3px gray;
}
/* .signupzone {
    display: flex;
    flex-direction: column;
    align-content: center;
    text-align: center;
    width: 500px;
    height: 700px;
    border: solid 1px gray;
    border-radius: 3px;
    margin-right: 10px;
    box-shadow: 3px 3px 3px 3px gray;
} */
.signup_h2 {
    color: #49c1a2;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 20px;
    font-size: large;
}
.sign_form {
  width: 300px;
  margin-left: 27px;
}

.sign_form label {
  display: flex;
  margin-top: 20px;
  font-size: 18px;
}

.sign_form input {
  width: 100%;
  padding: 7px;
  border: none;
  border: 1px solid gray;
  border-radius: 6px;
  outline: none;
}
.sign_input {
  width: 320px;
  height: 35px;
  margin-top: 30px;
  margin-left: 27px;
  border: none;
  background-color: #49c1a2;
  color: white;
  font-size: 18px;
}
</style>
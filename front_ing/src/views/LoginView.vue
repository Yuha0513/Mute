<template>
    <div>
        <h3>Login</h3>
        <form @submit.prevent>
            <label for="username">아이디 : </label>
            <input type="text" id="username" v-model="username">

            <label for="password">비밀번호 : </label>
            <input type="password" id="password" v-model="password">

            <input type="submit" value="logIn" @click="logIn">
        </form>
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

</style>
<template>
  <div>
    <form @submit.prevent>
        <label for="password1">새로운 비밀번호</label>
        <input type="password" v-model="password1">
        <label for="password2">비밀번호 확인</label>
        <input type="password" v-model="password2">

        <input type="submit" value="변경" @click="changePassword">

    </form>
  </div>
</template>

<script>
export default {
    name: 'PasswordChange',
    data() {
        return {
            password1: null,
            password2: null,
        }
    },
    methods: {
        changePassword() {
            const payload = {
                new_password1: this.password1,
                new_password2: this.password2,
            }
        this.$store.dispatch('changePassword', payload)
        }
    }
}
</script>

<style>

</style>
<template>
  <div>
    <div>
        <label for="selfimg">프로필</label>
        <input type="text" v-model="selfimg">
    </div>
    <div>
        <label for="selfimg">프로필2</label>
        <input type="text" v-model="otherimg">
    </div>
    <div>
        <label for="selfimg">자기소개</label>
        <input type="text" v-model="selfintroduce">
    </div>
    <button @click="updateUserDetail">submit</button>
  </div>
</template>

<script>
export default {
    name: 'UserUpdate',
    data() {
        return {
            selfimg: null,
            otherimg: null,
            selfintroduce: null,
        }
    },
    methods: {
        getUserDetail() {
            this.selfimg = this.$store.state.userDetail.selfimg
            this.otherimg = this.$store.state.userDetail.otherimg
            this.selfintroduce = this.$store.state.userDetail.selfintroduce
        },
        updateUserDetail() {
            const payload = {
                selfimg: this.selfimg,
                otherimg: this.otherimg,
                selfintroduce: this.selfintroduce,
            }
            this.$store.dispatch('updateUserDetail', payload)
            this.$store.dispatch('makeUserPic', this.selfimg,)
        }
    },
    created() {
        this.getUserDetail()
    }
}
</script>

<style>

</style>
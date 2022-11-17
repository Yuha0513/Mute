<template>
  <div>
    user
    {{ userInfo.username }}
    <button v-if="is_followed === false" @click="followFunc">follow</button>
    <button v-if="is_followed === true" @click="followFunc">unfollow</button>
  </div>
</template>

<script>
export default {
    name: 'UserView',
    // methods: {
    //   getUser() {
    //     this.$store.dispatch('getUser')
    //   }
    // },
    computed: {
      userInfo() {
        return this.$store.getters.userInfo
      },
      is_followed() {
        return this.$store.state.is_followed
      }
    },
    created() {
      this.$store.dispatch('getUser')
    },
    methods: {
      followFunc() {
        this.$store.dispatch('followFunc')
      }
    },
}
</script>

<style>

</style>
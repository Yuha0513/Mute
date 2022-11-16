<template>
  <div>
    user
    {{ userInfo }}
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
      }
    },
    created() {
      this.$store.dispatch('getUser')
    }
}
</script>

<style>

</style>
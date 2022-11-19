<template>
  <div> 좋아요 한 영화
    <button @click="getGenre">장르불러오기</button>
  </div>
</template>

<script>
export default {
  name: 'LikeList',
  created() {
    this.$store.dispatch('getLikeMovie')
  },
  methods: {
    getGenre() {
      this.$store.dispatch('getGenre')
    }
  }
}
</script>

<style>

</style>
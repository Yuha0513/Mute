<template>
  <div>

    <LikeMovieItem
      v-for="like in likeMovie"
      :key="like.id"
      :movie="like"
    />
  </div>


</template>

<script>
import LikeMovieItem from '@/components/User/LikeMovieItem'

export default {
  name: 'LikeList',
  components: {
    LikeMovieItem
  },
  data() {
    return {
      selected: '',
    }
  },
  created() {
    this.$store.dispatch('getLikeMovie')
  },
  computed: {
    likeMovie() {
      return this.$store.state.like_movie
    }
  }



}
</script>

<style>

</style>
<template>
  <div>
    <img :src="movie_poster" class="random_poster">
    {{ random.title }}
  </div>
</template>

<script>
export default {
  name: 'RandomMovieItem',
  props: {
    random: Object,
  },
  computed: {
    movie_poster() {
      const item = this.random
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ item?.poster_path }` 
    }
  },


}
</script>

<style>
.random_poster {
  width: 500px;
  height: 700px;
}
</style>
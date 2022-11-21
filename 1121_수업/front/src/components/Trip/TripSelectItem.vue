<template>
  <li>
    <img :src="movie_poster" width="500px">
    {{ countryRandomMovie.title }}
  </li>
</template>

<script>
export default {
  name: 'TripSelectItem',
  props: {
    countrymovie: Array
  },
  computed: {
    movie_poster() {
      const item = this.countrymovie[0]
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ item?.poster_path }` 
    },
    countryRandomMovie() {
      const movie = this.countrymovie[0]
      return movie
    }
  }
  
}
</script>

<style>

</style>
<template>
  <div> 좋아요 한 영화
    <ul 
      v-for="(selectmovie, index) in selectedGenreMovie"
      :key="index"
    >
    <li>
      <!-- <img :src="poster_url"> -->
      {{ selectmovie.title }}
    </li>
    </ul>
    <div
      v-for="genre in genres"
      :key="genre.id"
    >
    
      <button @click="selectGenre(genre, $event)">{{ genre.name }}</button>
    </div>
  </div>
</template>

<script>


export default {
  name: 'LikeList',
  data() {
    return {
      selected: '',
      poster_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.selectmovie.poster_path }`
    }
  },
  created() {
    this.$store.dispatch('getLikeMovie')
    this.$store.dispatch('getGenre')
  },
  methods: {
    selectGenre(event) {
      this.$store.dispatch('selectGenre', event)
    }
  },
  computed: {
    genres() {
      return this.$store.state.genres
    },
    selectedGenreMovie() {
      return this.$store.state.select_genre_movies
    }
  },


}
</script>

<style>

</style>
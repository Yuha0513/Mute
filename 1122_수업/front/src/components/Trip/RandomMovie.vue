<template>
  <div>
    <div class="select_genre">
      <div
      v-for="genre in genres"
      :key="genre.id"
    >
        <button @click="selectGenre(genre, $event)" class="genre_button">{{ genre.name }}</button>
      </div>
    </div>
    <div class="recommand_random_movie">
      <RandomMovieItem
      :random="selectedGenreMovie[0]"
      />

    </div>
    
  </div>
</template>

<script>
import _ from 'lodash'
import RandomMovieItem from '@/components/Trip/RandomMovieItem'

export default {
  name: 'RandomMovie',
  components: {
    RandomMovieItem
  },
  methods: {
    selectGenre(event) {

      this.$store.dispatch('selectGenre', event)
      this.$store.dispatch('getLikeMovie')
    }
  },
  computed: {
    genres() {
      return this.$store.state.genres
    },
    selectedGenreMovie() {
      return _.sampleSize(this.$store.state.select_genre_movies, 1)
    }
  },
  created() {
    // this.$store.dispatch('getLikeMovie')
    this.$store.dispatch('getGenre')
  },


}
</script>

<style>
.select_genre {
  display: flex;
  align-items: center;
  justify-content: center;
}
.genre_button {
  margin-right: 5px;
}
</style>
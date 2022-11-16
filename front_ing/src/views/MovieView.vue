<template>
  <div>

    <div v-for="movie in movies" :key="movie.id">
        {{ movie.title }}
        <router-link :to="{ name: 'detail', params: { id:movie.id }}"> detail </router-link>
        <hr>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieView',
    computed: {
        movies() {
            return this.$store.state.movies
        },
    },
    methods: {
        getMovies() {
            this.$store.dispatch('getMovies')
        }
    },
    created() {
        this.getMovies()
    }
}
</script>

<style>

</style>
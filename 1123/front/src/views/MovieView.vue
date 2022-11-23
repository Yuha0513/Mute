<template>
  <div>
    <div class="cardlist">
        <div class="row row-cols-6 row-cols-md-6 g-3">
        <MoviePoster
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
        />
        </div>
        
    </div>
  </div>
</template>

<script>
import MoviePoster from '@/components/MoviePoster'

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
    },
    components: {
        MoviePoster
    }
}
</script>

<style>
.cardlist {
    margin-top: 20px;

}
.box {
    width: 200px;
    height: 200px;
}
.movie_button {
    color: black;
}
.cardlist {
    margin-left: 150px;
}
</style>
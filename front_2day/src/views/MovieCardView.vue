<template>
  <div>
    <!-- <img :src="movie.poster_path"> -->
    {{ movie }}
    <MovieComment
    :movieID="movie?.id"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MovieComment from '@/components/MovieComment'

const API_URL = 'http://127.0.0.1:8000'



export default {
    name: 'MovieCardView',
    data() {
        return {
            movie: null,
            
        }
    },
    methods: {
        getMovieDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/movies/movies/${this.$route.params.id}`
            })
            .then((res) => {
                this.movie = res.data
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
    created() {
        this.getMovieDetail()
    },
    components: {
        MovieComment
    }

}
</script>

<style>

</style>
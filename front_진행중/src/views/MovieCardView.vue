<template>
  <div>
    <div class='movie_detail'>
        {{movie?.title}}
    </div>
    <div class="review_box">
        <MovieReview
        :movieID="movie.id"
        />
    </div>
 
  </div>
</template>

<script>
import axios from 'axios'
import MovieReview from '@/components/MovieReview'

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
        },
        // getToken: function () {
        //     const token = localStorage.getItem('jwt')
        //     const config = {
        //         headers: {
        //         Authorization: `JWT ${token}`
        //         },
        //     }
        //     return config
        // },
        },
    created() {
        this.getMovieDetail()
    },
    components: {
        MovieReview
    },
    

}
</script>

<style>
.movie_detail {
    display: flex;
    justify-content: center;
    align-items: center;
}
.review_box {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>
<template>
  <div>
    <div class='movie_detail'>
        <img :src=movie_poster>
        {{movie?.title}}
        <button @click="postLikeMovies">like</button>
    </div>
    <hr>
    <div>
        <YoutubeList
        :movyoutube=movie_Youtube
        />
    </div>
    <hr>
    <div class="review_box">
        <MovieReview
        :movieID="movie?.id"
        />
    </div>
 
  </div>
</template>

<script>
import axios from 'axios'
import MovieReview from '@/components/MovieReview'
import YoutubeList from '@/components/YoutubeList'

const API_URL = 'http://127.0.0.1:8000'


export default {
    name: 'MovieCardView',
    data() {
        return {
            movie: null,
            movie_poster: null,
            movie_Youtube: null,
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
                this.movie_Youtube = res.data.title
                this.movie_poster = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${res.data.poster_path}`
            })
            .catch((err) => {
                console.log(err)
            })
        },
        postLikeMovies() {
            this.$store.dispatch('postLikeMovies', this.movie)
        }
    },
    created() {
        this.getMovieDetail()
        console.log(this?.movie)
        this.movie_poster = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie.poster_path }`
        
    },
    components: {
        MovieReview, YoutubeList
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
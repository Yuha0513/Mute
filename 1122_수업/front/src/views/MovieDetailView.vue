<template>
  <div class="detail_body">
    <div class="second_body">
        <div class="movie_posterzone">
            <img :src=movie_poster width="300px">
        </div>
        <div class="movie_detail">
            <MovieActor
                v-for="(actor, index) in movie.actors"
                :key="index"
                :actor="actor"
            />
        </div>
    </div>
    <div class="third_body">
        <div class="bottom_youtubezone">
            <YoutubeList
            :movyoutube=movie.title
            />
        </div>
    </div>
    <div class="forth_body">
        <div class="review_zone">
            <MovieReview
            :movieID="this.movie.id"
            />
        </div>
    </div>

    

  </div>

</template>

<script>
import axios from 'axios'
import MovieReview from '@/components/MovieReview'
import YoutubeList from '@/components/YoutubeList'
import MovieActor from '@/components/Movie/MovieActor'

const API_URL = 'http://127.0.0.1:8000'


export default {
    name: 'MovieDetilView',
    data() {
        return {
            movie: null,
            movie_poster: null,
            movie_Youtube: null,
            movie_id: null,
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
                this.movie_id = res.data.id
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
        this.movie_poster = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie?.poster_path }`
        
    },
    components: {
        MovieReview, YoutubeList, MovieActor
    },
    computed: {
        movieActor() {
            return this.movie.actors
        }
    },
}
</script>

<style>



</style>
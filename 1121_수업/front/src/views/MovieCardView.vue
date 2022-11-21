<template>
  <div>
    <div class='movie_detail'>
        <img :src=movie_poster width="300px">
        <div class="movie_content">
            <p>{{movie?.title}}</p>
            <i @click="postLikeMovies" class="fa-sharp fa-solid fa-heart" ></i>
            <p>{{ movie?.vote_average }}</p>
            <p>{{ movie?.release_date }}</p>
            <p>{{ movie?.overview }}</p>

        </div>
    </div>
    <hr>
    <div>
        <YoutubeList
        :movyoutube=movie.title
        />
    </div>
    <hr>
    <div class="review_box">
        <MovieReview
        :movieID="this.movie.id"
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
.movie_content {
    width: 500px;
}

</style>
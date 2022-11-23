<template>
    <div>
        <div class="detail_body">
        <div class="second_body">
            <div class="movie_posterzone">
                <img :src=movie_poster width="400px">
            </div>
            <div class="movie_detail">
                <span class="movie_detail_title">{{movie?.title}}</span> 
                <span @click="postLikeMovies" class="fa-sharp fa-solid fa-heart" ></span>
                <button @click="getlikemovie">get</button>
                {{ like_ing }}
                <hr>
                <p>
                    <MovieActor
                    v-for="(actor, index) in movie.actors"
                    :key="index"
                    :actor="actor"
                    class="actor_name"
                />
                </p>
                <p class='movie_p'>{{ movie?.vote_average }}</p>
                <p class='movie_p'>{{ movie?.release_date }}</p>
                <p class='detail_overview'>{{ movie?.overview }}</p>
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
    </div>
  
</template>
  
  <script>
  import axios from 'axios'
  import MovieReview from '@/components/MovieReview'
  import YoutubeList from '@/components/YoutubeList'
  import MovieActor from '@/components/Movie/MovieActor'
  
  const API_URL = 'http://127.0.0.1:8000'
  
  
  export default {
      name: 'MovieCardView',
      data() {
          return {
              movie: null,
              movie_poster: null,
              movie_Youtube: null,
              movie_id: null,
              like_ing: false,
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
                  this.$store.dispatch('checkLikeMovie', res.data.id)
                  
              })
              .catch((err) => {
                  console.log(err)
              })
          },
          postLikeMovies(event) {
              this.$store.dispatch('postLikeMovies', this.movie)
            //   this.$store.dispatch('getLikeMovie')
              this.checkLikeMovie()
              if (this.like_ing === true) {
                event.target.style = 'color: red'
              } else {
                console.log('no')
              }
          },
          checkLikeMovie() {
            const check = this.$store.state.likeing
            if (check === true) {
                this.like_ing = true
                
            } else if (check === false) {
                this.like_ing = false
            }
        },
        getlikemovie() {
            this.$store.dispatch('getLikeMovie')
        },
      },
      created() {
          this.getMovieDetail()
          this.movie_poster = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie?.poster_path }`
          this.getlikemovie()
          this.checkLikeMovie()
      },
      components: {
          MovieReview, YoutubeList, MovieActor
      },
      computed: {
          movieActor() {
              return this.movie.actors
          },
          likemovie() {
            return this.$store.state.like_movie
          },
          movieID() {
            return this.movie?.id
          }
      },
  }
  </script>
  
<style>
.detail_body {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.second_body {
    width: 1500px;
    margin-top: 60px;
    margin-bottom: 150px;
    margin-left: 33px;
    /* margin-left: px; */
}
.movie_posterzone{
    float: left;
    width: 400px;
    height: 500px;
    margin-right: 250px;
}
.movie_detail {
    margin-left: 400px;
    text-align: left;
    width: 800px;
    height: 500px;
}
.third_body {
    margin-bottom: 20px;
}
.bottom_youtubezone {

}
.review_zone {

    
}
.movie_detail_title {
    margin-top: 25px;
    font-size: large;
    font-weight: bold;
    margin-bottom: 20px;
    margin-right: 20px;
}
.actor_name {
    margin-right: 5px;
    margin-top: 15px;
    margin-bottom: 20px;
}
.movie_p {
    margin-bottom: 7px;
}
.detail_overview {
    margin-top: 50px;
}
.liking {
    border: solid black;
    color:red;
}
</style>
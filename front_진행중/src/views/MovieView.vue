<template>
  <div>
    <div v-for="movie in movies" :key="movie.id">

        {{ movie.title }}
        <MoviePoster
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
        />

        <button class="movie_button"><router-link :to="{ name: 'detail', params: { id:movie.id }}"> detail </router-link></button>
    </div>
  </div>
</template>

<script>
import MoviePoster from '@/components/MoviePoster'
// import 'swiper/dist/css/swiper.css'
// import { swiper, swiperSlide } from 'vue-awesome-swiper'

export default {
    name: 'MovieView',
    computed: {
        movies() {
            return this.$store.state.movies
        },
        poster() {
            return this.image_url
        }
    },
    data() {
        return{
            image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/`
        }
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
    // components: {
    //     swiper,
    //     swiperSlide
    // },
    // data() {
    //     return {
    //         swiperOption: {
    //         slidesPerView: 5,
    //         spaceBetween: 50,
    //         pagination: {
    //         el: ".swiper-pagination",
    //         clickable: true
    //         },
    //         breakpoints: {
    //         1024: {
    //             slidesPerView: 4,
    //             spaceBetween: 40
    //         },
    //         768: {
    //             slidesPerView: 3,
    //             spaceBetween: 30
    //         },
    //         640: {
    //             slidesPerView: 2,
    //             spaceBetween: 20
    //         },
    //         320: {
    //             slidesPerView: 1,
    //             spaceBetween: 10
    //         }
    //     }
    //   }
    //     }
    // }
}
</script>

<style>
.swiper {
    border: 1px solid black;
}
.box {
    width: 200px;
    height: 200px;
}
.movie_button {
    color: black;
}
</style>
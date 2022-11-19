<template>

      <div class="col">
        <div class="card" @click="goMovieDetail">
          <img :src="movie_poster" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{movie.title}}</h5>
            <p class="card-text">{{ movie.release_data }}</p>
            <p class="card-text">{{ movie.vote_average }}</p>
          </div>
        </div>
      </div>


    <!-- <div class='movie_list_box'>
      <div class="movie_card"> -->
        <!-- <img :src="movie_poster" alt="Avatar" style="width:100%"> -->
        <!-- <div class="movie_container">
          <h4><b @click="goMovieDetail">{{movie.title}}</b></h4>
          <p>내용</p>
        </div>
      </div>
    </div> -->

</template>

<script>


export default {
  name:'MoviePoster',
  props: {
    movie: Object,
  },
  data() {
    return {
      movie_poster : `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie.poster_path }` 
    }
  },
  methods: {
    goMovieDetail() {
      this.$router.push({ name: 'detail', params: { id:this.movie.id }})
    }
  }

}
</script>

<style>
.movie_list_box {
  width: 600px;
}
.movie_card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 200px;
}
.movie_card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
.movie_container {
  padding: 2px 16px;
}
</style>
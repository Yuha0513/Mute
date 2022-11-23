<template>
  <div>
    <div class="select_genre">
      <div
      v-for="genre in genres"
      :key="genre.id"
    >
        <button @click="selectGenre(genre, $event)" class="big-button_genre" data-bs-toggle="modal" data-bs-target="#exampleModal2">{{ genre.name }}</button>
      </div>
      <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered ">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-4" id="exampleModalLabel">{{selectedGenreMovie[0]?.title}}</h1>
                <button type="button" class="btn-close btn-light" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <!-- <TripSelectItem
                  :countrymovie="random_country"
                /> -->
                <div>
                  <img :src="poster" width="200px" class="modal_img">
                  <p class="mt-4">
                    <span class="badge text-bg-success mx-1 mb-3" v-for="(ge, index) in genre" :key="index">{{ ge }}</span>
                    <!-- <span v-for="(ge, index) in genre" :key="index">{{ ge }} </span> -->
                  </p>
                  <p>개봉 일자 : {{ selectedGenreMovie[0]?.release_date }}</p>
                  <p>평점 : {{ selectedGenreMovie[0]?.vote_average }}</p>
                </div>
                <p class="mt-4">{{ selectedGenreMovie[0]?.overview}}</p>
                <!-- {{ random_country }} -->
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="goThisMovie">Go</button>
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
    </div>

  </div>
</template>

<script>
import _ from 'lodash'
// import RandomMovieItem from '@/components/Genre/RandomMovieItem'

export default {
  name: 'RandomMovie',
  components: {
    // RandomMovieItem
  },
  methods: {
    selectGenre(event) {

      this.$store.dispatch('selectGenre', event)
      this.$store.dispatch('getLikeMovie')
    },
    goThisMovie() {
      this.$router.push({ name: 'detail', params: { id:this.selectedGenreMovie[0].id }})
    },
  },
  computed: {
    genres() {
      return this.$store.state.genres
    },
    selectedGenreMovie() {
      return _.sampleSize(this.$store.state.select_genre_movies, 1)
    },
    poster() {
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.selectedGenreMovie[0].poster_path }`
    }
  },
  created() {
    // this.$store.dispatch('getLikeMovie')
    this.$store.dispatch('getGenre')
  },


}
</script>

<style>
.select_genre {
  display: flex;
  align-items: center;
  justify-content: center;
}
.genre_button {
  margin-right: 5px;
}
.big-button_genre{
  width: 90px;
  height: 50px;
  /* padding: 1em 2em; */
  border: 2px solid var(--colorShadeA);
  border-radius: 1em;
  background: var(--colorShadeE);
  transform-style: preserve-3d;
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
}
button.big-button_genre::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--colorShadeC);
  border-radius: inherit;
  box-shadow: 0 0 0 2px var(--colorShadeB), 0 0.75em 0 0 var(--colorShadeA);
  transform: translate3d(0, 0.75em, -1em);
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
}

button.big-button_genre:hover {
  background: var(--colorShadeD);
  transform: translate(0, 0.375em);
}

button.big-button_genre:hover::before {
  transform: translate3d(0, 0.75em, -1em);
}

button.big-button_genre:active {
  transform: translate(0em, 0.75em);
}

button.big-button_genre:active::before {
  transform: translate3d(0, 0, -1em);

  box-shadow: 0 0 0 2px var(--colorShadeB), 0 0.25em 0 0 var(--colorShadeB);
}
</style>
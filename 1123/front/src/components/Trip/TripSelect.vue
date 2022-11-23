<template>
  <div>
    <div>
      <div class="help-tip">
        <p>현재 가능한 나라
          <br>
        <br>  미국 중국 일본 한국 우크라이나 네덜란드 스페인 인도 포르투갈 프랑스 독일 영국</p>
      </div>
      <TripMap
      data-bs-toggle="modal" data-bs-target="#exampleModal1"
      />
    </div>
    <div class="country_movies" >
      <div class="modal fade" id="exampleModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered ">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-4" id="exampleModalLabel">{{random_country[0]?.title}}</h1>
              <button type="button" class="btn-close btn-light" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <!-- <TripSelectItem
                :countrymovie="random_country"
              /> -->
              <div>
                <img :src="random_poster" width="200px" class="modal_img">
                <p class="mt-4">
                  <span class="badge text-bg-success mx-1 mb-3" v-for="(ge, index) in genre" :key="index">{{ ge }}</span>
                  <!-- <span v-for="(ge, index) in genre" :key="index">{{ ge }} </span> -->
                </p>
                <p>개봉 일자 : {{ random_country[0]?.release_date }}</p>
                <p>평점 : {{ random_country[0]?.vote_average }}</p>
              </div>
              <p class="mt-4">{{ random_country[0]?.overview}}</p>
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
// import TripSelectItem from '@/components/Trip/TripSelectItem'

import TripMap from '@/components/Trip/TripMap'
import _ from 'lodash'

export default {
  name: 'TripSelect',
  data() {
    return {
      isModalViewed:false,
      genre: [],
    }
  },
  components: {
    // TripSelectItem, 
    TripMap
  },
  computed: {
    countries() {
      return this.$store.state.country
    },
    countrymovies() {
      return this.$store.state.country_movie
    },
    random_country() {
      return _.sampleSize(this.$store.state.country_movie, 1)
    },
    random_poster() {
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.random_country[0]?.poster_path }`
    },
    random_is() {
      return this.random_country.length
    }
  },
  methods: {
    clearTrip() {
      this.$store.dispatch('clearTrip')
    },
    goThisMovie() {
      this.$router.push({ name: 'detail', params: { id:this.random_country[0].id }})
    },
    changeGenre() {
      const genreid = this.random_country[0].genres
      const allgenre = this.$store.state.genres
      genreid.forEach(genre => {
        allgenre.forEach(all => {
          if(all.id === genre) {
            this.genre.push(all.name)
          }
        });
      });
    }
  },
  mounted() {
    this.changeGenre()

  }
}
</script>

<style>
.modal-content{
  background-color: #1E2021;
  color: white;

}
.modal-body{
  display: flex;
  flex-direction: column;
}
.modal_img{
  float: left;
}
.btn-close{
  color: white;
}


.help-tip{
margin-top: 100px;
top: 18px;
right: 18px;
text-align: center;
background-color: #BCDBEA;
border-radius: 50%;
width: 24px;
height: 24px;
font-size: 14px;
line-height: 26px;
cursor: default;
}



.help-tip:before{

content:'?';

font-weight: bold;

color:#fff;

}



.help-tip:hover p{

display:block;

transform-origin: 100% 0%;



-webkit-animation: fadeIn 0.3s ease-in-out;

animation: fadeIn 0.3s ease-in-out;



}



.help-tip p{

display: none;

text-align: left;

background-color: #1E2021;

padding: 20px;

width: 300px;

position: relative;

border-radius: 3px;

box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);

right: -4px;

color: #FFF;

font-size: 13px;

line-height: 1.4;

}



.help-tip p:before{

/* position: absolute; */

content: '';

width:0;

height: 0;

border:6px solid transparent;

border-bottom-color:#1E2021;

right:10px;

top:-12px;

}



.help-tip p:after{

width:100%;

height:40px;

content:'';

position: absolute;

top:-40px;

left:0;

}



</style>
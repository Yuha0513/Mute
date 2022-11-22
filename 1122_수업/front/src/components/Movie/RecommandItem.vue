<template>
  <div>

      <swiper-slide   swiper-slide>
        {{ recommand.title }}
      </swiper-slide>

  </div>

</template>

<script>
import { SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'RecommandItem',
  props: {
      recommand: Object,
  },
  data() {
    return {
      poster: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.recommand.poster_path }` ,
      // swiperOption: { 
      //   slidesPerView: 1, 
      //   spaceBetween: 30, 
      //   loop: true, 
      //   pagination: { 
      //       el: '.swiper-pagination', 
      //       clickable: true 
      //   }, 
      //   navigation: { 
      //       nextEl: '.swiper-button-next', 
      //       prevEl: '.swiper-button-prev' 
      //   } 
      // },
    }
  },
  components:	{

      SwiperSlide
  },
}
</script>

<style>
.reco_box {
  width: 32%;
  height: auto;
  border: 1px solid #ccc;
  margin-right: 1%;
  background: white;
  border-radius: 10px;
  transition: 0.9;
}
.reco_box:hover{
    box-shadow: 0 0 11px rgba(33, 33, 33, 0.5);
    cursor: pointer;
}
</style>
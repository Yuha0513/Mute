<template>
    <div class="reco_container">
        <swiper 
            class="swiper"
            :options="swiperOption"
            >
            <swiper-slide   swiper-slide
            v-for="recommand in Recommands"
            :key="recommand.id"
            class="swipermovie_card"
        >
            <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ recommand.poster_path }`" width="150px">
            {{ recommand.title }}

            </swiper-slide>
        <div 
            class="swiper-pagination"
            slot="pagination"
        >
        </div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-button-next"></div>

        <div class="swiper-scrollbar"></div>
        </swiper>
    <!-- <RecommandItem
        v-for="recommand in Recommands"
        :key="recommand.id"
        :recommand="recommand"
    /> -->
  </div>
        


  
</template>


<script>
// import RecommandItem from '@/components/Movie/RecommandItem'
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
    name: 'RecommandMovie',
    components: {
        // RecommandItem,
        Swiper,
        SwiperSlide,
    },
    methods: {
        getRecommand() {
            this.$store.dispatch('getRecommand')
        }
    },
    computed: {
        Recommands() {
            return this.$store.state.recommandMovie.movies
        },
        Recommands_poster() {
            return this.recommand
        }
    },
    created() {
        this.getRecommand()
    },
    data() {
        return {
            swiperOption: { 
                slidesPerView: 3, 
                spaceBetween: 30, 
                loop: true, 
                pagination: { 
                    el: '.swiper-pagination', 
                    clickable: true 
                }, 
                navigation: { 
                    nextEl: '.swiper-button-next', 
                    prevEl: '.swiper-button-prev' 
                },
                scrollbar: {
                    el: '.swiper-scrollbar',
                },
            },
        }
    },
    // swiperOption: { 
    //     slidesPerView: 2, 
    //     spaceBetween: 30, 
    //     loop: true, 
    //     pagination: { 
    //         el: '.swiper-pagination', 
    //         clickable: true 
    //     }, 
    //     navigation: { 
    //         nextEl: '.swiper-button-next', 
    //         prevEl: '.swiper-button-prev' 
    //     },
    //     scrollbar: {
    //         el: '.swiper-scrollbar',
    //     },
    // },
    
}
</script>

<style>
.reco_container {
    display: flex;
    width: 920px;
    height: auto;
    margin: 30px auto;
}
.swipermovie_card {
	height: 200px;
	width: 80px;
	border-radius: 15px;
	display: inline-block;
	margin-top: 30px;
	margin-left: 30px;
	margin-bottom: 30px;
	position: relative;
	box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
	overflow: hidden;
}
.swiper {
    height: 300px;
}
</style>
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'




Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_API = 'AIzaSyCtKyasqUV71di9blJvH4oM1oLYI9WUjgc' 


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    country: ['en', 'Germany', 'Ukraine', 'India', 'Spain', 'China', 'Netherlands', 'Portugal', 'Japan', 'France' ],
    language: ['en', 'de', 'te', 'ja', 'es', 'fr', 'zh', 'nl', 'pt', 'uk'],
    movies: [],
    token: null,
    user: null,
    isLogined: false,
    is_followed: false,
    reviews: null,
    youtubeVideos: [],
    genres: [],
    select_genre_movies: [],
    like_movie: [],
    selected_language: '',
    country_movie: [],
    userDetail: null,
    recommandMovie: [],
    otherInfo: [],
    likeing: false,
  },
  getters: {
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
    userInfo: (state) => state.user,
    reviews: (state) => state.reviews,
    genres: (state) => state.genres,

  },
  mutations: {
    GET_MOVIES: (state, movies) => state.movies = movies,
    SAVE_TOKEN(state, token) {
      state.token = token 
      state.isLogined = true
      router.push({ name: 'home' })
    },
    SET_USER: (state, user) => state.user = user,
    GET_REVIEW (state, reviews) {
      state.reviews = reviews
    },
    GET_YOUTUBE: (state, res) => state.youtubeVideos = res.data.items,
    DELETE_TOKEN(state) {
      state.token = ''
      state.isLogined = false
    },
    GET_GENRE (state, genres) {
      state.genres = genres
    } ,
    SELECT_GENRE(state, movies) {
      state.select_genre_movies = movies
    },
    GET_LIKE_MOVIE: (state, likemovie) => state.like_movie = likemovie,
    SELECT_COUNTRY(state, language) {
      state.selected_language = language

    },
    COUNTRY_MOVIE(state, movie_list) {
      state.country_movie = movie_list
    },
    MAKE_USER_DETAIL: (state, payload) => state.userDetail = payload,
    UPDATE_USER_DETAIL: (state, payload) => state.userDetail = payload,
    GET_RECOMMAND: (state, recommand) => state.recommandMovie = recommand,
    // CLEAR_TRIP(state) {
    //   state.country_movie = [],
    //   state.select_genre_movies = []
    // },
    GET_OTHER_INFO: (state, info) => state.otherInfo = info,
    CHECK_FOLLOWER: (state, payload) => state.is_followed = payload
  },
  
  actions: {
    // 영화 리스트 가져오기
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/movies/`,
      })
      .then((res) => {
        context.commit('GET_MOVIES', res.data)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 로그인 관련
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {...payload},
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        router.push({name: 'userdetail'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {...payload}
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        router.push({ name: 'user'})
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
        const error = JSON.stringify(err.response.data)
        alert(error)
      })
    },
    getUser({commit, getters}) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: getters.authHeader,
      })
      .then((res) => {
        commit('SET_USER', res.data)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout({commit, getters}) {
      axios({
        url: `${API_URL}/accounts/logout/`,
        method: 'post',
        headers: getters.authHeader,
      })
      .then((res) => {
        res
        commit('DELETE_TOKEN')
        commit('SET_USER', {})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    changePassword(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        data: {...payload},
        headers: context.getters.authHeader,
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    followFunc(context) {
      context.commit('FOLLOW_FUNC')
    },

    // 리뷰 관련
    createReview({getters, state, dispatch}, payload) {
      axios({
        method: 'post',
        url:`${API_URL}/movies/${payload.movieID}/review_list_create/`,
        data: {
          user: state.user.pk,
          title: state.user.pk,
          content: payload.content
        },
        headers: getters.authHeader
      })
      .then((res) => {
        console.log(res)
        dispatch('getReview',payload.movieID )
        // router.push({name: 'detail', params: { id:payload.movieID }})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReview({commit, getters}, movieID) {
      axios({
        method: 'get',
        url:`${API_URL}/movies/${movieID}/review_list_create`,
        headers: getters.authHeader,
      })
      .then((res) => {
        commit('GET_REVIEW', res.data)
        
      })
      .catch((err) => {
        console.log(err)
      })
    },
    reviewDelete({getters, dispatch}, payload) {
      axios({
        method: 'delete',
        url:`${API_URL}/movies/review/${payload.event.id}/`,
        headers: getters.authHeader,
        data: {...payload.event},
      })
      .then((res) => {
        console.log(res)
        dispatch('getReview',payload.movieID )
      })
      .catch((err) => {
        console.log(err)
      })
    },
    reviewUpdate({state, getters, dispatch}, payload) {
      const update = {
        title: state.user.pk,
        content: payload.newcontent
      }
      console.log(update)
      axios({
        method: 'put',
        url:`${API_URL}/movies/review/${payload.reviewId}/`,
        headers: getters.authHeader,
        data: { ...update },
      })
      .then((res) => {
        console.log(res)
        dispatch('getReview',payload.movieID)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // Movie Detail 에 들어갈 유튜브
    getYoutube(context, searchText) {
      const params = {
        q: searchText+'Trailer',
        key: YOUTUBE_API,
        part: 'snippet',
        type: 'video',
      }
      axios({
        method: 'get',
        url: YOUTUBE_URL,
        params,
      })
      .then((res) => {
        context.commit('GET_YOUTUBE', res)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    //알고리즘에 들어갈 좋아요
    postLikeMovies({getters, state, dispatch}, movie) {
      // console.log(state.user.pk)
      // console.log(movie.title)
      axios({
        method: 'post',
        url: `${API_URL}/movies/${state.user.pk}/${movie.title}/like/`,
        data: {
          user_id: state.user.pk,
          movie_id: movie.id,
        },
        headers: getters.authHeader,
      })
      .then((res) => {
        console.log(res)
        dispatch('getLikeMovie')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikeMovie({commit,getters}) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/yourmovie/`,
        headers: getters.authHeader,
      })
      .then((res) => {
        commit('GET_LIKE_MOVIE', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    checkLikeMovie(context, movieid) {
      const likemovies = context.state.like_movie
      likemovies.forEach(like => {
        if(like.id == movieid) {
          context.state.likeing = true
        } else {
          context.state.likeing = false
        }
      });
    },

    //장르 랜덤
    getGenre(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/genres/`,
        headers: context.getters.authHeader,
      })
      .then((res) => {
        context.commit('GET_GENRE', res.data)

      })
      .catch((err) => {
        console.log(err)
      })
    },
    selectGenre(context, genre) {
      const selectmovieList = []
      context.state.movies.forEach(function(movie) {
        movie.genres.forEach(function(element) {
          if (element === genre.id) {
            selectmovieList.push(movie)
          }
        })
        // context.commit('SELECT_GENRE', payload)
      })
      context.commit('SELECT_GENRE', selectmovieList)
      // console.log(selectmovieList) 
    },
    selectCountry(context, selectedcountry) {
      let select_language = ''
      if (selectedcountry === 'United States of America') {
        select_language = 'en'
      } else if (selectedcountry === 'Germany') {
        select_language = 'de'
      } else if (selectedcountry === 'Ukraine') {
        select_language = 'uk'
      } else if (selectedcountry === 'India') {
        select_language = 'te'
      } else if (selectedcountry === 'Spain') {
        select_language = 'es'
      } else if (selectedcountry === 'China') {
        select_language = 'zh'
      } else if (selectedcountry === 'Netherlands') {
        select_language = 'nl'
      } else if (selectedcountry === 'Portugal') {
        select_language = 'pt'
      } else if (selectedcountry === 'Japan') {
        select_language = 'ja'
      } else if (selectedcountry === 'France') {
        select_language = 'fr'
      } else if (selectedcountry === 'South Korea') {
        select_language = 'ko'
      } else if (selectedcountry === 'United Kingdom') {
        select_language = 'en'
      } else {
        alert('아직 영화가 설정되지 않았습니다!')
      }
      context.commit('SELECT_COUNTRY', select_language)
    //   const country_movie = []
    //   context.state.movies.forEach(function(movie) {
    //     if (movie.original_language === select_language) {
    //       console.log(movie)
    //       // country_movie.push(movie)
    //     }
    //     context.commit('SELECT_COUNTRY', country_movie)
    // })
    },
    countryMovie(context) {
      let movie_list = []
      context.state.selected_language
      context.state.movies.forEach(function(movie) {
        if (movie.original_language === context.state.selected_language) {
          movie_list.push(movie)
        }
      context.commit('COUNTRY_MOVIE', movie_list)
      // movie_list = []
      })
    },
    makeUserDetail(context, payload) {
      context.commit('MAKE_USER_DETAIL', payload)
      router.push({name: 'home'})
    },
    updateUserDetail(context, payload) {
      context.commit('UPDATE_USER_DETAIL', payload)
      // router.push({name: 'user'})
    },
    getRecommand(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/recommend/`,
        headers: context.getters.authHeader,
      })
      .then((res) => {
        // console.log(res)
        context.commit('GET_RECOMMAND', res.data)

      })
      .catch((err) => {
        console.log(err)
      })
    },
    makeUserPic(context, userpic) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/profilepic/`,
        headers: context.getters.authHeader,
        data: {
          image: userpic
        }
      })
      .then((res) => {
        console.log('보냄')
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUserPic(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profilepic/`,
        headers: context.getters.authHeader,
      })
      .then((res) => {
        console.log('보냄')
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getOtherInfo(context,username) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${username}/`,
        headers: context.getters.authHeader,
      })
      .then((res) => {
        let info = res.data
        context.commit('GET_OTHER_INFO', info)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    followUser(context) {
      const myId = context.state.user.pk
      const userid = context.state.otherInfo.id
      axios({
        method: 'post',
        url: `${API_URL}/accounts/follow/${myId}/${userid}/`,
        headers: context.getters.authHeader,
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    checkfollower(context) {
      const followers = context.state.otherInfo.followers
      followers.forEach(follower => {
        if (follower === context.state.user.pk) {
          console.log('있음')
          context.commit('CHECK_FOLLOWER', true)
        } else {
          console.log('없음')
          context.commit('CHECK_FOLLOWER', false)
        }
      });
    },

  },
  modules: {
  }
})

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
    movies: [],
    token: null,
    user: null,
    isLogined: false,
    is_followed: false,
    reviews: null,
    youtubeVideos: [],
    genres: [],
    select_genre_movies: [],
  },
  getters: {
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
    userInfo: (state) => state.user,
    isLogin(state) {
      if (state.token) {
        state.isLogined = true
      } else {
        state.isLogined = false
      }
    },
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
    FOLLOW_FUNC(state) {
      if (state.is_followed === false) {
        state.is_followed = true
      } else {
        state.is_followed = false
      }
    },
    GET_REVIEW (state, reviews) {
      state.reviews = reviews
    },
    GET_YOUTUBE: (state, res) => state.youtubeVideos.push(res.data.items),
    DELETE_TOKEN: (state) => state.token = '',
    GET_GENRE (state, genres) {
      state.genres = genres
    } ,
    SELECT_GENRE(state, movie) {
      if (state.select_genre_movies.length === 0) {
        state.select_genre_movies.push(movie)
      }
      else if (state.select_genre_movies.length >= 1) {
        state.select_genre_movies = []
        state.select_genre_movies.push(movie)
      }
      console.log(movie)
    },
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
    followFunc(context) {
      context.commit('FOLLOW_FUNC')
    },

    // 리뷰 관련
    createReview({getters, state}, payload) {
      axios({
        method: 'post',
        url:`${API_URL}/movies/${payload.movieID}/review_list_create/`,
        data: {
          user: state.user.pk,
          title: payload.title,
          content: payload.content
        },
        headers: getters.authHeader
      })
      .then((res) => {
        console.log(res)
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
    reviewDelete({getters}, review) {
      axios({
        method: 'delete',
        url:`${API_URL}/movies/review/${review.id}/`,
        headers: getters.authHeader,
        data: {...review},
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // Movie Detail 에 들어갈 유튜브
    getYoutube(context, searchText) {
      const params = {
        q: searchText+'movie',
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
        // console.log(res.data.items)
        context.commit('GET_YOUTUBE', res)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    //알고리즘에 들어갈 좋아요
    postLikeMovies({getters, state}, movie) {
      console.log(state.user.pk)
      console.log(movie.title)
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
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikeMovie({getters}) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/yourmovie/`,
        headers: getters.authHeader,
      })
      .then((res) => {
        getters
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getGenre(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/genres/`,
        headers: context.getters.authHeader,
      })
      .then((res) => {
        context.commit('GET_GENRE', res.data)
        console.log(this.genres)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // selectGenre({state, getters}, genre) {
    //   console.log(state.user.pk)
    //   console.log(genre.id)
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/movies/${state.user.pk}/${genre.name}/like/`,
    //     headers: getters.authHeader,
    //     data: {
    //       user_id: state.user.pk,
    //       genre_id: genre.id
    //     }
    //   })
    //   .then((res) => {
    //     console.log(res)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // }
    selectGenre(context, genre) {
      context.state.movies.forEach(function(movie) {
        movie.genres.forEach(function(element) {
          if (element === genre.id) {
            context.commit('SELECT_GENRE', movie)
          }
        })
        // context.commit('SELECT_GENRE', payload)
        })
      
    }
  },
  modules: {
  }
})

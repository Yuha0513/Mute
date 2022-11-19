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
    reviews: (state) => state.reviews
  },
  mutations: {
    GET_MOVIES: (state, movies) => state.movies = movies,
    SAVE_TOKEN(state, token) {
      state.token = token 
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
    GET_YOUTUBE: (state, res) => state.youtubeVideos = res.data.items
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
        url: `${API_URL}/accounts/users/`,
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
        commit('SET_TOKEN', '')
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
    }
  },
  modules: {
  }
})

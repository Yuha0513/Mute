import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    token: null,
    user: null,
    isLogined: false,
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
    }
  },
  mutations: {
    GET_MOVIES: (state, movies) => state.movies = movies,
    SAVE_TOKEN(state, token) {
      state.token = token 
      router.push({ name: 'home' })
    },
    SET_USER: (state, user) => state.user = user,
  },
  actions: {
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
      })
      .catch((err) => {
        console.log(err)
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
        commit('SET_TOKEN', '')
        commit('SET_USER', {})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})

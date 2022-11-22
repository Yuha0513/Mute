import Vue from 'vue'
import testView from '../views/testView'
import VueRouter from 'vue-router'
import TripView from '../views/TripView'
import UserView from '../views/UserView'
import LoginView from '../views/LoginView'
import MovieView from '../views/MovieView'
import HomeView from '../views/HomeView.vue'
import UserDetail from '../views/UserDetail'
import SignupView from '../views/SignupView'
import UserUpdate from '../views/UserUpdate'
import OtherProfile from '../views/OtherProfile'
import MovieCardView from '../views/MovieCardView'
import PasswordChange from '../views/PasswordChange'
import MovieDetailView from '../views/MovieDetailView'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/movies',
    name: 'movies',
    component: MovieView
  },
  {
    path:'/trip',
    name: 'trip',
    component: TripView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/userupdate',
    name: 'userupdate',
    component: UserUpdate
  },
  {
    path: '/userdetail',
    name: 'userdetail',
    component: UserDetail
  },
  {
    path: '/password',
    name: 'password',
    component: PasswordChange
  },
  {
    path:'/detail',
    name:'moviedetail',
    component: MovieDetailView
  },
  {
    path:'/user',
    name: 'user',
    component: UserView
  },
  {
    path:'/test',
    name:'test',
    component: testView
  },
  {
    path:'/otheruser/:username',
    name: 'otheruser',
    component: OtherProfile
  },
  {
    path:'/movies/:id',
    name: 'detail',
    component: MovieCardView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

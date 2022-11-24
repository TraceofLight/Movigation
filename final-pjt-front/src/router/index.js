import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FeaturedView from '../views/FeaturedView.vue'
import SearchView from '../views/SearchView.vue'
import ReviewView from '../views/ReviewView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import ProfileView from '../views/ProfileView.vue'
import SignupView from '../views/SignupView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/featured',
    name: 'Featured',
    component: FeaturedView
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView
  },
  {
    path: '/review',
    name: 'Review',
    component: ReviewView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

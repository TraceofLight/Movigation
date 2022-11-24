// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {

  state: {
  },
  
  getters: {
    isLoggedIn: state => !!state.token,
    isNotLoggedIn: state => state.token == '',
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    loginAuthError: state => state.loginAuthError,
    signupAuthError: state => state.signupAuthError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
  },

  actions: {
    fetchProfile({ commit, getters }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },
  },
}

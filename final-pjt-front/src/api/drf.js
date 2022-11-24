const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // googleAuth: () => HOST + ACCOUNTS + 'google/',
  },
  movies: {
    movie: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/`,
  },
}
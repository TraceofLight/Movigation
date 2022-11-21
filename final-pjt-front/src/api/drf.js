const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const DRF = 'dj-rest-auth/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + DRF + 'login/',
    logout: () => HOST + ACCOUNTS + DRF + 'logout/',
  },
  movies: {
    movie: TMDBMovieId => HOST + MOVIES + `${TMDBMovieId}/`,
  },
}
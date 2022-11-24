<template>
  <div class="col">
  <ModalView v-if="isModalViewed" @close-modal="isModalViewed=false">
    <MovieDetail :movieId="movie.id || movie.tmdb_movie_id" :movieName="movie.title || movie.name"/>
  </ModalView>
  <div class="flip-card" @click="isModalViewed=true, showModal()">
    <div class="card-front">
      <figure>
        <div class="img-bg"></div>
        <img :src="posterPath" />
      </figure>
    </div>

    <div class="card-back">
      <figure>
        <div class="img-bg"></div>
        <img :src="posterPath" />
      </figure>

      <ul class="card-ul">
        <li>{{ movie.title || movie.name }}</li>
        <div class="star-box">
          <i :id="idPath" data-id="1" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="2" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="3" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="4" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="5" class="fa-solid fa-star"></i>
        </div>
      </ul>
    </div>
  </div>
  </div>
</template>

<script>
import ModalView from "@/components/ModalView.vue"
import MovieDetail from "@/components/MovieDetail.vue"
import notFoundImg from '@/assets/404-not-found.png'

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  components: {
    ModalView,
    MovieDetail,
  },
  data: function () {
    return {
      isModalViewed: false,
    }
  },
  methods: {
    showModal () {
      document.body.classList.add("modal-open");
    },
  },
  computed: {
    posterPath: function () {
      const poster_path = this.movie.poster_path
      if (poster_path) {
        return `https://image.tmdb.org/t/p/original/${poster_path}`
      } else {
        return notFoundImg
      }
    },
    idPath: function () {
      return `movie-${ this.movie.id || this.movie.tmdb_movie_id }`
    }
  },
  mounted() {
    const voteAverage = Math.round(this.movie.vote_average / 2)
    const stars = document.querySelectorAll(`#movie-${ this.movie.id || this.movie.tmdb_movie_id }`)
    for(let star of stars) {
      const num = star.dataset.id
      if(voteAverage - num >= 0) {
        if (!star.classList.contains('star-active')) {
          star.classList.add('star-active')
        }
      } 
    }
  },
  updated() {
    const voteAverage = Math.round(this.movie.vote_average / 2)
    const stars = document.querySelectorAll(`#movie-${ this.movie.id || this.movie.tmdb_movie_id }`)
    for(let star of stars) {
      const num = star.dataset.id
      if(voteAverage - num >= 0) {
        if (!star.classList.contains('star-active')) {
          star.classList.add('star-active')
        }
      } else {
        if (star.classList.contains('star-active')) {
          star.classList.remove('star-active')
        }
      }
    }
  }
}
</script>

<style>
.body {
  background-image: none;
}

</style>
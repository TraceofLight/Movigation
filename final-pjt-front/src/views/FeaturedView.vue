<template>
    <v-container>
      <MovieCarousel/>
      <MovieList/>
    </v-container>
</template>

<script>

  import MovieCarousel from '../components/MovieCarousel.vue'
  import MovieList from '../components/MovieList.vue'

  export default {
    name: 'FeaturedView',
    components: {
      MovieCarousel,
      MovieList,
    },
  }
</script>

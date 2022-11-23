<template>
    <v-container>
      <MovieCarousel/>
    <v-main class="grey lighten-2">
      <v-container>
        <v-row>
          <template v-for="n in 30">
            <v-col
              :key="n"
              class="mt-2"
              cols="12"
            >
              <strong>Category {{ n }}</strong>
            </v-col>

            <v-col
              v-for="j in 6"
              :key="`${n}${j}`"
              cols="6"
              md="2"
            >
              <v-sheet height="250"></v-sheet>
            </v-col>
          </template>
        </v-row>
      </v-container>
    </v-main>
  </v-container>
</template>

<script>

  import MovieCarousel from '../components/MovieCarousel.vue'

  export default {
    name: 'FeaturedView',
    components: {
      MovieCarousel
    },
  }
</script>

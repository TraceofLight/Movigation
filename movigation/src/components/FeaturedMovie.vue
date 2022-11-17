<template>
  <v-card
    elevation="24"
    max-width="444"
    class="mx-auto"
  >
    <v-system-bar lights-out></v-system-bar>
    <v-carousel
      :continuous="false"
      :cycle="cycle"
      :show-arrows="false"
      hide-delimiter-background
      delimiter-icon="mdi-minus"
      height="300"
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
        <v-sheet
          :color="colors[i]"
          height="100%"
          tile
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <div class="text-h2">
              {{ slide }} Slide
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <v-list two-line>
      <v-list-item>
        <v-list-item-avatar>
          <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title>John Leider</v-list-item-title>
          <v-list-item-subtitle>Author</v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-action>
          <v-switch
            v-model="cycle"
            label="Cycle Slides"
            inset
          ></v-switch>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>

  import axios from 'axios'

  axios.get({
    url: 'https://api.themoviedb.org/3/trending/movie/week',
    api_key: `${process.env.VUE_APP_TOKEN}`,
  })
    .then(
      function(response) {
        console.log(response)
      }
    )
    .catch(error => {
      console.log(error)
    })
// function range(start, end) {
//   const result_arr = []
//   for (let i = start; i < end; i ++) {
//     result_arr.push(i)
//   }
//   return result_arr
// }

// const thumbnailLinks = [
//   {urls: "https://placeimg.com/200/200/animals?1"},
//   {urls: "https://placeimg.com/200/200/animals?2"},
//   {urls: "https://placeimg.com/200/200/animals?3"},
//   {urls: "https://placeimg.com/200/200/animals?4"},
//   {urls: "https://placeimg.com/200/200/animals?5"},
//   {urls: "https://placeimg.com/200/200/animals?6"},
//   {urls: "https://placeimg.com/200/200/animals?7"},
//   {urls: "https://placeimg.com/200/200/animals?8"},
//   {urls: "https://placeimg.com/200/200/animals?9"},
//   {urls: "https://placeimg.com/200/200/animals?10"},
//   {urls: "https://placeimg.com/200/200/animals?11"},
// ]

  export default {
    data () {
      return {
        colors: [
          'green',
          'secondary',
          'yellow darken-4',
          'red lighten-2',
          'orange darken-1',
        ],
        cycle: false,
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
      }
    },
  }
</script>

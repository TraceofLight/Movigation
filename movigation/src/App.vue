<template>
  <v-container class="d-flex mx-2">
    <div id="app" class="d-flex">
      <MovieNavbar/>
      <div id="logo-box" class="d-flex">
        <img src="@/assets/sample.png" style="width: 100%">
      </div>
      <div class="d-flex my-3">
        <h1>Movigator</h1>
        <br>
        <h1>Find Your Best Movie</h1>
      </div>
    </div>
  </v-container>
</template>

<script>
import MovieNavbar from '@/components/MovieNavbar.vue'

export default {
  components: {
    MovieNavbar,
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');

#app {
  font-family: 'Nanum Gothic', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 15px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #87CEEB;
    }
  }
}
</style>

<template>
  <div id="app">
    <nav >
      <v-app-bar class="d-flex flex-row">
        <v-app-bar-nav-icon>
          <v-icon color="blue">mdi-movie-play</v-icon>
        </v-app-bar-nav-icon>
        <div class="">Movigator</div>
        <v-spacer></v-spacer>
        <div width="250">
          <router-link to="/" class="mx-3">Home</router-link> | 
          <router-link to="/calendar" class="mx-3">Calendar</router-link> | 
          <router-link to="/about" class="mx-3">Search</router-link>
        </div>
      </v-app-bar>
    </nav>
    <router-view/>
  </div>
</template>

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
      color: #42b983;
    }
  }
}
</style>

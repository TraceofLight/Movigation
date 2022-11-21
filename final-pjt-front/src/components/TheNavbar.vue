<template>
  <v-container>
    <nav>
      <v-app-bar app elevate-on-scroll>

        <template v-slot:img="{ props }">
          <v-img v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
          src="@/assets/nav-bg.jpg"></v-img>
        </template>

        <router-link class="d-flex" style="text-decoration: none;" to="/">
          <v-btn plain>
            <v-icon style="color: black;">mdi-movie-play</v-icon>
            <v-toolbar-title style="color: black;" class="ml-5">Movigator</v-toolbar-title>
          </v-btn>
        </router-link>

        <v-spacer></v-spacer>

          <router-link style="text-decoration: none; color: black;" :to="{ name: 'Featured'}">
            <v-btn class="mx-2" plain>
              Featured
            </v-btn>
          </router-link>

          <router-link style="text-decoration: none; color: black;" to="/search">
            <v-btn class="mx-2" plain>
              Search
            </v-btn>
          </router-link>

          <router-link style="text-decoration: none; color: black;" to="/review">
            <v-btn class="mx-2" plain>
              Review
            </v-btn>
          </router-link>

        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        fixed
        temporary
        right
      >
        <router-link style="text-decoration: none;" to="/">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link style="text-decoration: none;" to="/profile">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>
        </router-link>
        
        <router-link style="text-decoration: none;" to="/login">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-login</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link style="text-decoration: none;" to="/logout">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </router-link>

      </v-navigation-drawer>
    </nav>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {
        drawer: null,
      }
    },
  }
</script>

<template>
  <v-container>
    <LoginPage />
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
            <v-toolbar-title style="color: black;" class="ml-5">Movigation</v-toolbar-title>
          </v-btn>
        </router-link>

        <v-spacer/>

          <router-link style="text-decoration: none; color: black;" :to="{ name: 'Featured' }">
            <v-btn class="mx-2" plain>
              Featured
            </v-btn>
          </router-link>

          <router-link style="text-decoration: none; color: black;" :to="{ name: 'Search' }">
            <v-btn class="mx-2" plain>
              Search
            </v-btn>
          </router-link>

          <router-link style="text-decoration: none; color: black;" :to="{ name: 'Review' }">
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
        <router-link style="text-decoration: none;" :to="{ name: 'Home' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link style="text-decoration: none;" :to="{ name: 'Profile' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>
        </router-link>
        
        <v-list-item :to="{ name: 'Login' }">
          <v-list-item-icon>
            <v-icon>mdi-login</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item>

        <v-list-item link @click="logout()">
          <v-list-item-icon>
            <v-icon>mdi-logout</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item>

      </v-navigation-drawer>
      <router-view/>
    </nav>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import drf from '@/api/drf'

  export default {

    name: 'TheNavbar',

    components: {
    },

    data() {
      return {
        drawer: false,
      }
    },

    methods: {
      testLogout() {
        axios({
          url: drf.accounts.logout(),
          method: "post",
        })
      }
    }
  }
</script>

<style>
</style>

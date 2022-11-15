<template>
  <nav>
    <v-app-bar class="d-flex flex-row">
      <v-app-bar-nav-icon>
        <router-link style="text-decoration: none;" to="/" class="mx-3"><v-icon>mdi-movie-play</v-icon></router-link>
      </v-app-bar-nav-icon>
      <v-toolbar-title style="font-weight: bold;" class="ml-3">Movigator</v-toolbar-title>
      <v-spacer></v-spacer>
      <router-link style="text-decoration: none;" to="/calendar" class="mx-3"><v-btn icon><v-icon>mdi-calendar</v-icon></v-btn></router-link>
      <router-link style="text-decoration: none;" to="/account" class="mx-3"><v-btn icon><v-icon>mdi-account</v-icon></v-btn></router-link>
    </v-app-bar>
  </nav>
</template>
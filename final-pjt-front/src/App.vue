<template>
  <v-app class="d-flex">
    <TheNavbar/>
  </v-app>
</template>

<script>

  export default {
    components: {
      TheNavbar: () => import('./components/TheNavbar.vue')
    },
  }

</script>

<style>

</style>
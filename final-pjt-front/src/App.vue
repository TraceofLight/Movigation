<template>
  <v-app>
    <TheNavbar/>
    <HomeView/>
  </v-app>
</template>

<script>
  import TheNavbar from '@/components/TheNavbar'
  import HomeView from '@/views/HomeView'

  export default {
    components: {
      TheNavbar,
      HomeView,
    },
  }

</script>
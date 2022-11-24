<template>
  <v-container id="logoutView">
  </v-container>
</template>

<script>

  import { mapActions } from 'vuex'
  import router from '@/router'

  export default {
    name: 'LogoutView',
    data() {
      return {
      }
    },
    computed: {
      ...mapActions(['logout'])
    },
    mounted() {
      window.onload=function() {
        this.logout
      }
      router.push({ name: 'Home' })
      location.reload()
    },
  }

</script>

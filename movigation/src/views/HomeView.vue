<template>
  <div class="home">
    <FeaturedMovie/>
  </div>
</template>

<script>

import FeaturedMovie from '@/components/FeaturedMovie.vue'

export default {
  name: 'HomeView',
  components: {
    FeaturedMovie,
  }
}
</script>

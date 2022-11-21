<template>
  <v-container>
    <v-main class="grey lighten-2">
      <v-container>
        <v-row>
          <template v-for="n in 5">
            <v-col
              :key="n"
              class="mt-2"
              cols="12"
            >
              <strong>Category {{ n }}</strong>
            </v-col>

            <v-col
              v-for="j in 6"
              :key="`${n}${j}`"
              cols="6"
              md="2"
            >
              <v-sheet height="150"></v-sheet>
            </v-col>
          </template>
        </v-row>
      </v-container>
    </v-main>
  </v-container>
</template>

<script>
  export default {
    name: 'HomeView',
    components: {
    },
  }
</script>

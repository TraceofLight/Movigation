<template>
    <nav>
        <v-app-bar class="d-flex">
            <router-link style="text-decoration: none;" to="/" class="mx-3">
                <v-icon>mdi-movie-play</v-icon>
            </router-link>
            <v-toolbar-title style="font-weight: bold;" class="ml-3">Movigator</v-toolbar-title>
            <v-spacer></v-spacer>
            <router-link style="text-decoration: none;" to="/calendar" class="mx-3">
                <v-btn icon>
                    <v-icon>mdi-calendar</v-icon>
                </v-btn>
            </router-link>
            <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    
            <v-navigation-drawer v-model="drawer" absolute temporary right>
                <v-list nav dense>
    
                    <v-list-item link>
                        <v-list-item-icon>
                            <v-icon>mdi-home</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Home</v-list-item-title>
                    </v-list-item>
    
                    <v-list-item link>
                        <v-list-item-icon>
                            <v-icon>mdi-calendar</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Calendar</v-list-item-title>
                    </v-list-item>
    
                    <v-list-item link>
                        <v-list-item-icon>
                            <v-icon>mdi-account</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Account</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-navigation-drawer>
        </v-app-bar>
    </nav>
</template>

<script>
export default {
    data: () => ({
        drawer: false,
        group: null,
    }),
}
</script>
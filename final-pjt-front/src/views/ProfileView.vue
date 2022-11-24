<template>
  <v-container fluid class="py-6" id="ProfileView">
    <div id="Profile">

    <div
      class="
        min-height-300
        border-radius-xl
        overflow-hidden
        position-relative
        mx-3
      "
      :style="`background-image: url('https://images.unsplash.com/photo-1531512073830-ba890ca4eba2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80'); background-position: 50%; background-size: cover;`"
    >
      <span class="mask bg-gradient-primary opacity-6"></span>
    </div>
    <v-card
      class="shadow px-4 py-4 mx-9 overflow-hidden border-radius-xl mt-n16"
    >
      <v-row>
        <v-col cols="auto">
          <v-avatar width="74" height="74" class="shadow border-radius-lg">
            <img
              src="@/assets/img/bruce-mars.jpg"
              alt="Avatar"
              class="border-radius-lg"
            />
          </v-avatar>
        </v-col>
        <v-col cols="auto" class="my-auto">
          <div class="h-100">
            <h5 class="mb-1 text-h5 text-typo font-weight-bold">
              Richard Devis
            </h5>
            <p class="mb-0 font-weight-light text-body text-sm">
              CEO / Co-Founder
            </p>
          </div>
        </v-col>
        <v-col lg="4" md="6" class="my-sm-auto ms-sm-auto me-sm-0 mx-auto mt-3">
          <v-tabs background-color="transparent" right>
            <v-tabs-slider></v-tabs-slider>

            <v-tab :ripple="false" href="#tab-1">
              <svg
                class="text-dark me-1"
                width="16px"
                height="16px"
                viewBox="0 0 42 42"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
              >
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(-2319.000000, -291.000000)"
                    fill="#FFFFFF"
                    fill-rule="nonzero"
                  >
                    <g transform="translate(1716.000000, 291.000000)">
                      <g transform="translate(603.000000, 0.000000)">
                        <path
                          class="color-background"
                          d="M22.7597136,19.3090182 L38.8987031,11.2395234 C39.3926816,10.9925342 39.592906,10.3918611 39.3459167,9.89788265 C39.249157,9.70436312 39.0922432,9.5474453 38.8987261,9.45068056 L20.2741875,0.1378125 L20.2741875,0.1378125 C19.905375,-0.04725 19.469625,-0.04725 19.0995,0.1378125 L3.1011696,8.13815822 C2.60720568,8.38517662 2.40701679,8.98586148 2.6540352,9.4798254 C2.75080129,9.67332903 2.90771305,9.83023153 3.10122239,9.9269862 L21.8652864,19.3090182 C22.1468139,19.4497819 22.4781861,19.4497819 22.7597136,19.3090182 Z"
                        ></path>
                        <path
                          class="color-background"
                          d="M23.625,22.429159 L23.625,39.8805372 C23.625,40.4328219 24.0727153,40.8805372 24.625,40.8805372 C24.7802551,40.8805372 24.9333778,40.8443874 25.0722402,40.7749511 L41.2741875,32.673375 L41.2741875,32.673375 C41.719125,32.4515625 42,31.9974375 42,31.5 L42,14.241659 C42,13.6893742 41.5522847,13.241659 41,13.241659 C40.8447549,13.241659 40.6916418,13.2778041 40.5527864,13.3472318 L24.1777864,21.5347318 C23.8390024,21.7041238 23.625,22.0503869 23.625,22.429159 Z"
                          opacity="0.7"
                        ></path>
                        <path
                          class="color-background"
                          d="M20.4472136,21.5347318 L1.4472136,12.0347318 C0.953235098,11.7877425 0.352562058,11.9879669 0.105572809,12.4819454 C0.0361450918,12.6208008 6.47121774e-16,12.7739139 0,12.929159 L0,30.1875 L0,30.1875 C0,30.6849375 0.280875,31.1390625 0.7258125,31.3621875 L19.5528096,40.7750766 C20.0467945,41.0220531 20.6474623,40.8218132 20.8944388,40.3278283 C20.963859,40.1889789 21,40.0358742 21,39.8806379 L21,22.429159 C21,22.0503869 20.7859976,21.7041238 20.4472136,21.5347318 Z"
                          opacity="0.7"
                        ></path>
                      </g>
                    </g>
                  </g>
                </g>
              </svg>
              <span class="ms-1">App</span>
            </v-tab>

            <v-tab :ripple="false" href="#tab-2">
              <svg
                class="text-dark me-1"
                width="16px"
                height="16px"
                viewBox="0 0 40 44"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
              >
                <title>document</title>
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(-1870.000000, -591.000000)"
                    fill="#FFFFFF"
                    fill-rule="nonzero"
                  >
                    <g transform="translate(1716.000000, 291.000000)">
                      <g transform="translate(154.000000, 300.000000)">
                        <path
                          class="color-background"
                          d="M40,40 L36.3636364,40 L36.3636364,3.63636364 L5.45454545,3.63636364 L5.45454545,0 L38.1818182,0 C39.1854545,0 40,0.814545455 40,1.81818182 L40,40 Z"
                          opacity="0.603585379"
                        ></path>
                        <path
                          class="color-background"
                          d="M30.9090909,7.27272727 L1.81818182,7.27272727 C0.814545455,7.27272727 0,8.08727273 0,9.09090909 L0,41.8181818 C0,42.8218182 0.814545455,43.6363636 1.81818182,43.6363636 L30.9090909,43.6363636 C31.9127273,43.6363636 32.7272727,42.8218182 32.7272727,41.8181818 L32.7272727,9.09090909 C32.7272727,8.08727273 31.9127273,7.27272727 30.9090909,7.27272727 Z M18.1818182,34.5454545 L7.27272727,34.5454545 L7.27272727,30.9090909 L18.1818182,30.9090909 L18.1818182,34.5454545 Z M25.4545455,27.2727273 L7.27272727,27.2727273 L7.27272727,23.6363636 L25.4545455,23.6363636 L25.4545455,27.2727273 Z M25.4545455,20 L7.27272727,20 L7.27272727,16.3636364 L25.4545455,16.3636364 L25.4545455,20 Z"
                        ></path>
                      </g>
                    </g>
                  </g>
                </g>
              </svg>
              <span class="ms-1">Messages</span>
            </v-tab>

            <v-tab :ripple="false" href="#tab-3">
              <svg
                class="text-dark me-1"
                width="16px"
                height="16px"
                viewBox="0 0 40 40"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
              >
                <title>settings</title>
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(-2020.000000, -442.000000)"
                    fill="#FFFFFF"
                    fill-rule="nonzero"
                  >
                    <g transform="translate(1716.000000, 291.000000)">
                      <g transform="translate(304.000000, 151.000000)">
                        <polygon
                          class="color-background"
                          opacity="0.596981957"
                          points="18.0883333 15.7316667 11.1783333 8.82166667 13.3333333 6.66666667 6.66666667 0 0 6.66666667 6.66666667 13.3333333 8.82166667 11.1783333 15.315 17.6716667"
                        ></polygon>
                        <path
                          class="color-background"
                          d="M31.5666667,23.2333333 C31.0516667,23.2933333 30.53,23.3333333 30,23.3333333 C29.4916667,23.3333333 28.9866667,23.3033333 28.48,23.245 L22.4116667,30.7433333 L29.9416667,38.2733333 C32.2433333,40.575 35.9733333,40.575 38.275,38.2733333 L38.275,38.2733333 C40.5766667,35.9716667 40.5766667,32.2416667 38.275,29.94 L31.5666667,23.2333333 Z"
                          opacity="0.596981957"
                        ></path>
                        <path
                          class="color-background"
                          d="M33.785,11.285 L28.715,6.215 L34.0616667,0.868333333 C32.82,0.315 31.4483333,0 30,0 C24.4766667,0 20,4.47666667 20,10 C20,10.99 20.1483333,11.9433333 20.4166667,12.8466667 L2.435,27.3966667 C0.95,28.7083333 0.0633333333,30.595 0.00333333333,32.5733333 C-0.0583333333,34.5533333 0.71,36.4916667 2.11,37.89 C3.47,39.2516667 5.27833333,40 7.20166667,40 C9.26666667,40 11.2366667,39.1133333 12.6033333,37.565 L27.1533333,19.5833333 C28.0566667,19.8516667 29.01,20 30,20 C35.5233333,20 40,15.5233333 40,10 C40,8.55166667 39.685,7.18 39.1316667,5.93666667 L33.785,11.285 Z"
                        ></path>
                      </g>
                    </g>
                  </g>
                </g>
              </svg>
              <span class="ms-1">Settings</span>
            </v-tab>
          </v-tabs>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card class="overflow-scroll">
            <div class="py-4 d-flex">
              <v-col lg="1" md="2" sm="3" cols="4" class="text-center">
                <v-avatar size="58" class="shadow-sm">
                  <v-icon class="material-icons-round">add</v-icon>
                </v-avatar>
                <p class="mb-0 text-sm text-body font-weight-light mt-2">
                  Add story
                </p>
              </v-col>
              <v-col
                v-for="avatar in stories"
                :key="avatar.user"
                lg="1"
                md="2"
                sm="3"
                cols="4"
                class="text-center"
              >
                <v-avatar size="58" class="border border-primary px-1 py-1">
                  <v-img :src="avatar.image" width="50" height="50"> </v-img>
                </v-avatar>
                <p class="mb-0 text-sm text-body font-weight-light mt-2">
                  {{ avatar.user }}
                </p>
              </v-col>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col lg="8" cols="12">
          <v-card>
            <div class="border-bottom d-flex align-center px-4 py-4">
              <div class="d-flex align-center">
                <a href="javascript:;" class="text-decoration-none">
                  <v-avatar size="48" class="rounded-circle">
                    <v-img
                      src="@/assets/img/team-4.jpg"
                      alt="profile-image"
                    ></v-img>
                  </v-avatar>
                </a>
                <div class="mx-4">
                  <a
                    href="javascript:;"
                    class="
                      text-dark
                      font-weight-600
                      text-sm text-decoration-none
                    "
                    >John Snow</a
                  >
                  <small class="d-block text-muted">3 days ago</small>
                </div>
              </div>
              <div class="text-end ms-auto">
                <v-btn
                  outlined
                  color="#fff"
                  class="font-weight-bolder bg-gradient-primary py-4 px-7"
                  small
                >
                  <v-icon size="8" class="material-icons-round pe-2"
                    >add</v-icon
                  >
                  Follow
                </v-btn>
              </div>
            </div>
            <div class="px-4 py-4">
              <p class="mb-6 text-body font-weight-light">
                Personal profiles are the perfect way for you to grab their
                attention and persuade recruiters to continue reading your CV
                because you’re telling them from the off exactly why they should
                hire you.
              </p>
              <v-img
                src="https://images.unsplash.com/photo-1578271887552-5ac3a72752bc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80"
                class="border-radius-lg shadow-lg"
              >
              </v-img>
              <v-row class="align-center px-2 mt-6 mb-2">
                <v-col sm="6">
                  <div class="d-flex">
                    <div class="d-flex align-center">
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >thumb_up</v-icon
                      >
                      <span class="text-sm text-body me-4">150</span>
                    </div>
                    <div class="d-flex align-center">
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >mode_comment</v-icon
                      >
                      <span class="text-sm text-body me-4">36</span>
                    </div>
                    <div class="d-flex align-center">
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >forward</v-icon
                      >
                      <span class="text-sm text-body me-4">12</span>
                    </div>
                  </div>
                </v-col>
                <v-col sm="6">
                  <div class="d-flex align-center">
                    <div class="d-flex align-items-center ms-auto">
                      <v-avatar size="24" class="border border-white ms-n2">
                        <img src="@/assets/img/team-5.jpg" alt="Avatar" />
                      </v-avatar>
                      <v-avatar size="24" class="border border-white ms-n2">
                        <img src="@/assets/img/team-2.jpg" alt="Avatar" />
                      </v-avatar>
                      <v-avatar size="24" class="border border-white ms-n2">
                        <img src="@/assets/img/team-1.jpg" alt="Avatar" />
                      </v-avatar>
                    </div>
                    <small class="ps-2 font-weight-bold text-body text-sm"
                      >and 30+ more</small
                    >
                  </div>
                </v-col>
              </v-row>
              <div class="mb-1">
                <hr class="horizontal dark mt-1 mb-5" />
                <div class="d-flex">
                  <div class="flex-shrink-0">
                    <v-avatar>
                      <v-img src="@/assets/img/bruce-mars.jpg"></v-img>
                    </v-avatar>
                  </div>
                  <div class="flex-grow-1 ms-4">
                    <h5 class="text-h5 text-typo font-weight-bold mt-0 mb-2">
                      Michael Lewis
                    </h5>
                    <p class="text-sm font-weight-light text-body">
                      I always felt like I could do anything. That’s the main
                      thing people are controlled by! Thoughts- their perception
                      of themselves!
                    </p>
                    <div class="d-flex align-center">
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >thumb_up</v-icon
                      >
                      <span class="text-sm me-2 text-body">3 likes</span>
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >share</v-icon
                      >
                      <span class="text-sm me-2 text-body">2 shares</span>
                    </div>
                  </div>
                </div>

                <div class="d-flex mt-5">
                  <div class="flex-shrink-0">
                    <v-avatar>
                      <v-img src="@/assets/img/team-5.jpg"></v-img>
                    </v-avatar>
                  </div>
                  <div class="flex-grow-1 ms-4">
                    <h5 class="text-h5 text-typo font-weight-bold mt-0 mb-2">
                      Jessica Stones
                    </h5>
                    <p class="text-sm font-weight-light text-body">
                      Society has put up so many boundaries, so many limitations
                      on what’s right and wrong that it’s almost impossible to
                      get a pure thought out. It’s like a little kid, a little
                      boy.
                    </p>
                    <div class="d-flex align-center">
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >thumb_up</v-icon
                      >
                      <span class="text-sm me-2 text-body">10 likes</span>
                      <v-icon
                        size="14"
                        class="
                          material-icons-round
                          me-1
                          text-body
                          cursor-pointer
                        "
                        >share</v-icon
                      >
                      <span class="text-sm me-2 text-body">1 share</span>
                    </div>
                  </div>
                </div>

                <div class="d-flex mt-6">
                  <div class="flex-shrink-0">
                    <v-avatar>
                      <v-img src="@/assets/img/team-4.jpg"></v-img>
                    </v-avatar>
                  </div>
                  <div class="flex-grow-1 ms-4">
                    <v-textarea
                      placeholder="Write your comment"
                      class="input-style mt-0 pt-0"
                      color="#e91e63"
                    ></v-textarea>
                  </div>
                </div>
              </div>
            </div>
          </v-card>
        </v-col>
        <v-col lg="4" cols="12">
          <v-card class="mb-6" v-for="card in cards" :key="card.title">
            <div class="px-4 py-4">
              <v-row class="align-center">
                <v-col cols="9">
                  <h5
                    class="
                      text-h5
                      font-weight-bold
                      mb-1
                      text-gradient text-primary
                    "
                  >
                    <a href="javascript:;" class="text-decoration-none">{{
                      card.title
                    }}</a>
                  </h5>
                </v-col>
                <v-col cols="3" class="text-end">
                  <v-menu
                    transition="slide-y-transition"
                    offset-y
                    offset-x
                    min-width="150"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        icon
                        :ripple="false"
                        class="text-secondary"
                        v-bind="attrs"
                        v-on="on"
                        small
                      >
                        <v-icon size="16">fas fa-ellipsis-v</v-icon>
                      </v-btn>
                    </template>

                    <v-list class="pa-2">
                      <v-list-item
                        class="list-item-hover-active border-radius-md"
                      >
                        <v-list-item-content class="pa-0">
                          <v-list-item-title
                            class="
                              text-body-2
                              ls-0
                              text-body
                              font-weight-600
                              py-2
                            "
                          >
                            Edit Team
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-list-item
                        class="list-item-hover-active border-radius-md"
                      >
                        <v-list-item-content class="pa-0">
                          <v-list-item-title
                            class="
                              text-body-2
                              ls-0
                              text-body
                              font-weight-600
                              py-2
                            "
                          >
                            Add Member
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-list-item
                        class="list-item-hover-active border-radius-md"
                      >
                        <v-list-item-content class="pa-0">
                          <v-list-item-title
                            class="
                              text-body-2
                              ls-0
                              text-body
                              font-weight-600
                              py-2
                            "
                          >
                            See Details
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <hr class="horizontal dark my-2" />
                      <v-list-item
                        class="list-item-hover-active border-radius-md"
                      >
                        <v-list-item-content class="pa-0">
                          <v-list-item-title
                            class="text-danger ls-0 font-weight-600 mb-0"
                          >
                            Remove Team
                          </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-menu>
                </v-col>
              </v-row>
              <p class="text-body font-weight-light mt-3">
                {{ card.description }}
              </p>
              <div class="d-flex">
                <p class="mb-0 font-weight-light text-body">Industry:</p>
                <v-btn
                  elevation="0"
                  small
                  :ripple="false"
                  height="21"
                  class="
                    border-radius-md
                    font-weight-bolder
                    px-3
                    py-3
                    badge-font-size
                    ms-auto
                    text-body
                  "
                  color="#e4e8ed"
                  >{{ card.industry }}</v-btn
                >
              </div>
              <hr class="horizontal dark my-4" />
              <div class="d-flex">
                <p class="mb-0 font-weight-light text-body">Rating:</p>
                <div class="rating ms-auto">
                  <v-icon size="16">fas fa-star text-body</v-icon>
                  <v-icon size="16">fas fa-star text-body ms-1</v-icon>
                  <v-icon size="16">fas fa-star text-body ms-1</v-icon>
                  <v-icon size="16">fas fa-star text-body ms-1</v-icon>
                  <v-icon size="16" v-if="card.rating == 'partial'"
                    >fas fa-star-half-alt text-body ms-1</v-icon
                  >
                  <v-icon size="16" v-if="card.rating == 'full'"
                    >fas fa-star text-body ms-1</v-icon
                  >
                </div>
              </div>
              <hr class="horizontal dark my-4" />
              <div class="d-flex">
                <p class="mb-0 font-weight-light text-body">Members:</p>
                <span class="avatar-group d-flex ms-auto">
                  <v-tooltip
                    bottom
                    color="#212529"
                    v-for="avatar in card.avatars"
                    :key="avatar.name"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-avatar
                        v-bind="attrs"
                        v-on="on"
                        size="24"
                        class="border border-white ms-n3"
                      >
                        <img :src="avatar.image" alt="Avatar" />
                      </v-avatar>
                    </template>
                    <span>{{ avatar.name }}</span>
                  </v-tooltip>
                </span>
              </div>
            </div>
          </v-card>

          <v-card class="mb-6" v-for="(card, i) in brands" :key="i">
            <div class="px-4 py-4">
              <div class="d-flex">
                <v-avatar>
                  <v-img :src="card.img"></v-img>
                </v-avatar>
                <div class="ms-2 my-auto">
                  <h6 class="mb-0 text-h6 text-typo font-weight-bold">
                    {{ card.title }}
                  </h6>
                  <p class="text-xs mb-0 text-body">{{ card.hour }}</p>
                </div>
              </div>
              <p class="text-body font-weight-light mt-3">
                {{ card.description }}
              </p>
              <div class="d-flex">
                <p class="mb-0 text-body">
                  <b>Meeting ID</b>:
                  <span class="font-weight-light">{{ card.id }}</span>
                </p>
              </div>
              <hr class="horizontal dark my-4" />
              <div class="d-flex">
                <v-btn
                  :elevation="0"
                  color="#cb0c9f"
                  class="
                    font-weight-bolder
                    btn-success
                    bg-gradient-default
                    py-4
                    px-4
                  "
                  small
                >
                  Join
                </v-btn>
                <span class="avatar-group d-flex ms-auto">
                  <v-tooltip
                    bottom
                    color="#212529"
                    v-for="avatar in card.avatars"
                    :key="avatar.name"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-avatar
                        v-bind="attrs"
                        v-on="on"
                        size="24"
                        class="border border-white ms-n3"
                      >
                        <img :src="avatar.image" alt="Avatar" />
                      </v-avatar>
                    </template>
                    <span>{{ avatar.name }}</span>
                  </v-tooltip>
                </span>
              </div>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
    </div>
    <div id="Settings" style="display: none;">
<v-row>
      <v-col lg="4" sm="8">
        <v-tabs background-color="transparent" class="text-left">
          <v-tabs-slider></v-tabs-slider>

          <v-tab :ripple="false" href="#tab-1">
            <span class="ms-1">Messages</span>
          </v-tab>

          <v-tab :ripple="false" href="#tab-2">
            <span class="ms-1">Social</span>
          </v-tab>

          <v-tab :ripple="false" href="#tab-3">
            <span class="ms-1">Notifications</span>
          </v-tab>

          <v-tab :ripple="false" href="#tab-4">
            <span class="ms-1">Backup</span>
          </v-tab>
        </v-tabs>
      </v-col>
    </v-row>
    <v-row class="px-4">
      <v-col lg="3">
        <v-card class="card-shadow border-radius-xl position-sticky top-1">
          <div class="px-4 pt-3 pb-0">
            <v-list>
              <v-list-item-group class="border-radius-sm">
                <v-list-item
                  class="px-3 py-1 border-radius-lg mb-2"
                  v-for="item in menu"
                  :key="item.icon"
                >
                  <v-icon
                    size="18"
                    class="material-icons-round me-2 text-dark"
                    >{{ item.icon }}</v-icon
                  >
                  <v-list-item-content class="py-0">
                    <a href="#profile" class="text-decoration-none">
                      <div class="d-flex flex-column">
                        <span class="text-dark text-sm">{{ item.text }}</span>
                      </div>
                    </a>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </div>
        </v-card>
      </v-col>
      <v-col lg="9">
        <v-card class="card-shadow px-4 py-4 overflow-hidden border-radius-xl">
          <v-row>
            <v-col cols="auto">
              <v-avatar width="74" height="74" class="shadow rounded-circle">
                <img
                  src="@/assets/img/bruce-mars.jpg"
                  alt="Avatar"
                  class="rounded-circle"
                />
              </v-avatar>
            </v-col>
            <v-col cols="auto" class="my-auto">
              <div class="h-100">
                <h5 class="mb-1 text-h5 text-typo font-weight-bold">
                  Alec Thompson
                </h5>
                <p class="mb-0 font-weight-light text-body text-sm">
                  CEO / Co-Founder
                </p>
              </div>
            </v-col>
            <v-col
              lg="4"
              md="6"
              class="my-sm-auto ms-sm-auto me-sm-0 mx-auto mt-3"
            >
              <div class="d-flex align-center">
                <p
                  class="mb-0 text-body text-xs ms-auto"
                  v-if="switche == true"
                >
                  Switch to invisible
                </p>
                <p
                  class="mb-0 text-body text-xs ms-auto"
                  v-if="switche == false"
                >
                  Switch to visible
                </p>
                <v-switch
                  :ripple="false"
                  class="mt-0 pt-0 ms-3 switch"
                  v-model="switche"
                  hide-details
                ></v-switch>
              </div>
            </v-col>
          </v-row>
        </v-card>
        <basic-info></basic-info>
        <change-password></change-password>
        <two-factor></two-factor>
        <accounts></accounts>
        <notifications></notifications>
        <sessions></sessions>
        <delete-account></delete-account>
      </v-col>
    </v-row>
    </div>
  </v-container>
</template>
<script>
export default {
  name: "ProfileView",
  data: function () {
    return {
      stories: [
        {
          image: require("@/assets/img/team-1.jpg"),
          user: "Abbie W",
        },
        {
          image: require("@/assets/img/team-2.jpg"),
          user: "Boris U",
        },
        {
          image: require("@/assets/img/team-3.jpg"),
          user: "Kay R",
        },
        {
          image: require("@/assets/img/team-4.jpg"),
          user: "Tom M",
        },
        {
          image: require("@/assets/img/team-5.jpg"),
          user: "Nicole N",
        },
        {
          image: require("@/assets/img/marie.jpg"),
          user: "Marie P",
        },
        {
          image: require("@/assets/img/bruce-mars.jpg"),
          user: "Bruce M",
        },
        {
          image: require("@/assets/img/ivana-squares.jpg"),
          user: "Sandra A",
        },
        {
          image: require("@/assets/img/kal-visuals-square.jpg"),
          user: "Katty L",
        },
        {
          image: require("@/assets/img/ivana-square.jpg"),
          user: "Emma O",
        },
        {
          image: require("@/assets/img/team-9.jpeg"),
          user: "Tao G",
        },
      ],
      cards: [
        {
          title: "Digital Marketing",
          description:
            "A group of people who collectively are responsible for all of the work necessary to produce working, validated assets.",
          industry: "Martketing Team",
          rating: "partial",
          avatars: [
            {
              image: require("@/assets/img/team-1.jpg"),
              name: "Elena Morison",
            },
            {
              image: require("@/assets/img/team-2.jpg"),
              name: "Ryan Milly",
            },
            {
              image: require("@/assets/img/team-3.jpg"),
              name: "Nick Daniel",
            },
            {
              image: require("@/assets/img/team-4.jpg"),
              name: "Peterson",
            },
          ],
        },
        {
          title: "Design",
          description:
            "Because it's about motivating the doers. Because I’m here to follow my dreams and inspire other people to follow their dreams, too.",
          industry: "Design Team",
          rating: "full",
          avatars: [
            {
              image: require("@/assets/img/team-4.jpg"),
              name: "Peterson",
            },
            {
              image: require("@/assets/img/team-3.jpg"),
              name: "Nick Daniel",
            },
            {
              image: require("@/assets/img/team-1.jpg"),
              name: "Elena Morison",
            },
            {
              image: require("@/assets/img/team-2.jpg"),
              name: "Ryan Milly",
            },
          ],
        },
      ],
      brands: [
        {
          img: require("@/assets/img/small-logos/logo-slack.svg"),
          title: "Slack Meet",
          hour: "11:00 AM",
          id: "902-128-281",
          description: "You have an upcoming meet for Marketing Planning",
          avatars: [
            {
              image: require("@/assets/img/team-1.jpg"),
              name: "Elena Morison",
            },
            {
              image: require("@/assets/img/team-2.jpg"),
              name: "Ryan Milly",
            },
            {
              image: require("@/assets/img/team-3.jpg"),
              name: "Nick Daniel",
            },
            {
              image: require("@/assets/img/team-4.jpg"),
              name: "Peterson",
            },
          ],
        },
        {
          img: require("@/assets/img/small-logos/logo-invision.svg"),
          title: "Invision",
          hour: "4:50 PM",
          id: "111-968-981",
          description:
            "You have an upcoming video call for Soft Design at 5:00 PM.",
          avatars: [
            {
              image: require("@/assets/img/team-3.jpg"),
              name: "Nick Daniel",
            },
            {
              image: require("@/assets/img/team-1.jpg"),
              name: "Elena Morison",
            },
            {
              image: require("@/assets/img/team-2.jpg"),
              name: "Ryan Milly",
            },
            {
              image: require("@/assets/img/team-4.jpg"),
              name: "Peterson",
            },
          ],
        },
      ],
    };
  },
};
</script>

<style scoped>
#ProfileView {
  margin-top: 64px;
}
</style>
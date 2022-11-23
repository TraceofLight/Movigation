<template>
  <v-container id="theNavbar">
    <div class="box d-flex mx-auto">
      <div class="box-part" id="bp-left">
        <div class="partition" id="partition-register">
          <div class="partition-title">REGISTER ACCOUNT</div>
          <div class="partition-form">
            <form autocomplete="false">
              <div class="autocomplete-fix">
                <input disabled type="password password2">
              </div>
              <input id="email" type="text" placeholder="Email">
              <input id="username" type="text" placeholder="Username">
              <input id="password" type="password" placeholder="Password">
              <input id="password2" type="password2" placeholder="Password Confirmation">
            </form>

            <div style="margin-top: 21px">
            </div>
            <button class="large-btn" @click="signup(payload)">Register</button>
            <router-link :to="{ name: 'Login' }">
              <button class="large-btn" id="goback-btn">GO BACK</button>
            </router-link>
            <router-view/>
          </div>
        </div>
      </div>
      <div class="box-part" id="bp-right">
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="10770">TV영화</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="878">SF</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="10751">가족</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="27">공포</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="99">다큐멘터리</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="18">드라마</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="10749">로맨스</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="12">모험</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="9648">미스터리</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="80">범죄</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="37">서부</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="53">스릴러</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="16">애니메이션</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="28">액션</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="36">역사</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="10402">음악</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="10752">전쟁</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="35">코미디</v-btn>
        <v-btn x-large @click="onSelectGenre" class="raise genre-button" data-id="14">판타지</v-btn>
      </div>
    </div>
  </v-container>
</template>

<script>

  import { mapActions, mapGetters } from 'vuex'

  const MODAL_WIDTH = 656

  export default {
    name: 'SignupView',
    data: function () {
      return {
        modalWidth: MODAL_WIDTH,
        payload: {
          genres: [],
          credentials: {
            email: '',
            username: '',
            password1: '',
            password2: '',
          },
      }}
    },
    created() {
      this.modalWidth =
        window.innerWidth < MODAL_WIDTH ? MODAL_WIDTH / 2 : MODAL_WIDTH
    },
    computed: {
      ...mapGetters(['signupAuthError'])
    },
    methods: {
      ...mapActions(['signup']),
      onSelectGenre: function (event) {
        const genreId = event.target.dataset.id
        const genreBtn = event.target
        if (!genreBtn.classList.contains('raise-focus')) {
          genreBtn.classList.add('raise-focus')
          this.payload.genres.push(genreId)
        } else {
          genreBtn.classList.remove('raise-focus')
          const idx = this.payload.genres.indexOf(genreId)
          this.payload.genres.splice(idx, 1)
        }
      }
    }
  }

</script>

<style lang="scss">

.box {
  background: white;
  overflow: hidden;
  width: 656px;
  height: 400px;
  border-radius: 2px;
  box-sizing: border-box;
  box-shadow: 0 0 40px black;
  color: #8b8c8d;
  font-size: 0;
  .box-part {
    display: inline-block;
    position: relative;
    vertical-align: top;
    box-sizing: border-box;
    height: 100%;
    width: 50%;
    &#bp-right {
      border-left: 1px solid #eee;
    }
  }
  .box-messages {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
  }
  .box-error-message {
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
    height: 0;
    line-height: 32px;
    padding: 0 12px;
    text-align: center;
    width: 100%;
    font-size: 11px;
    color: white;
    background: #f38181;
  }
  .partition {
    width: 100%;
    height: 100%;
    .partition-title {
      box-sizing: border-box;
      padding: 30px;
      width: 100%;
      text-align: center;
      letter-spacing: 1px;
      font-size: 20px;
      font-weight: 300;
    }
    .partition-form {
      padding: 0 20px;
      box-sizing: border-box;
    }
  }
  input[type='password'],
  input[type='password2'],
  input[type='text'] {
    display: block;
    box-sizing: border-box;
    margin-bottom: 4px;
    width: 100%;
    font-size: 12px;
    line-height: 2;
    border: 0;
    border-bottom: 1px solid #dddedf;
    padding: 4px 8px;
    font-family: inherit;
    transition: 0.5s all;
  }
  button {
    background: white;
    border-radius: 4px;
    box-sizing: border-box;
    padding: 10px;
    letter-spacing: 1px;
    font-family: 'Open Sans', sans-serif;
    font-weight: 400;
    min-width: 140px;
    margin-top: 8px;
    color: #8b8c8d;
    cursor: pointer;
    border: 1px solid #dddedf;
    text-transform: uppercase;
    transition: 0.1s all;
    font-size: 10px;
    &:hover {
      border-color: mix(#dddedf, black, 90%);
      color: mix(#8b8c8d, black, 80%);
    };
  }
  .large-btn {
    width: 100%;
    background: white;
    span {
      font-weight: 600;
    }
  }
  .autocomplete-fix {
    position: absolute;
    visibility: hidden;
    overflow: hidden;
    opacity: 0;
    width: 0;
    height: 0;
    left: 0;
    top: 0;
  }
}
.pop-out-enter-active,
.pop-out-leave-active {
  transition: all 0.5s;
}
.pop-out-enter,
.pop-out-leave-active {
  opacity: 0;
  transform: translateY(24px);
}
.genre-button {
  margin-top: 0;
}
</style>
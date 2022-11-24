<template>
  <v-container id="loginView">
    <div class="box d-flex mx-auto">
      <div class="box-part" id="bp-left">
        <div class="partition" id="partition-register">
          <div class="partition-title">LOGIN ACCOUNT</div>
          <div class="partition-form">
            <form autocomplete="false">

              <div class="autocomplete-fix">
                <input disabled type="password">
              </div>

              <!-- <input id="email" type="text" placeholder="Email"> -->
              <input v-model="credentials.username" type="text" placeholder="Username" required />
              <label>Username</label>

              <input @keypress.enter="login(credentials)" v-model="credentials.password" type="password" placeholder="Password" required />
              <label>Password</label>

            </form>

            <div style="margin-top: 21px"/>

            <div class="button-set">
              <button id="login-btn" @click.prevent="login(credentials)">SIGN IN</button>
              <router-link :to="{ name: 'Signup' }">
                <button id="register-btn" >Register</button>
              </router-link>
            </div>
            <div style="margin-top: 10px"/>
            <button class="large-btn github-btn">connect with <span>github</span></button>
            <button class="large-btn google-btn">connect with <span>google</span></button>
          </div>
        </div>
      </div>
      <div class="box-part" id="bp-right">
        <div class="box-messages">
        </div>
      </div>
    </div>
    <router-view/>
  </v-container>
</template>

<script>

  import { mapActions, mapGetters } from 'vuex'

  const MODAL_WIDTH = 656
  // const googleId = process.env.VITE_GOOGLE_OAUTH_CLIENT_ID
  // const googleRedirect = process.env.VITE_GOOGLE_OAUTH_REDIRECT

  export default {
    name: 'LoginView',
    data() {
      return {
        modalWidth: MODAL_WIDTH,
        // googleId: googleId,
        // googleRedirect: googleRedirect,
        credentials: {
          'username': '',
          'password': '',
        },
      }
    },
    computed: {
      ...mapGetters(['signupAuthError'])
    },
    created() {
      this.modalWidth =
        window.innerWidth < MODAL_WIDTH ? MODAL_WIDTH / 2 : MODAL_WIDTH
    },
    methods: {
      ...mapActions(['login']),
    }
  }
</script>
<style lang="scss">

#loginView {
  padding-top: 11%;
};

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
      background: url('@/assets/login-bg.png') no-repeat top left;
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
    }
  }
  .large-btn {
    width: 100%;
    background: white;
    span {
      font-weight: 600;
    }
    &:hover {
      color: white !important;
    }
  }
  .button-set {
    margin-bottom: 8px;
  }
  #register-btn,
  #signin-btn {
    margin-left: 8px;
  }
  .google-btn {
    border-color: #4285f4;
    color: #4285f4;
    &:hover {
      border-color: #4285f4;
      background: #4285f4;
    }
  }
  .github-btn {
    border-color: #dba226;
    color: #dba226;
    &:hover {
      border-color: #dba226;
      background: #dba226;
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
</style>
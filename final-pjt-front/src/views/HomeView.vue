<template>
  <v-container class="d-flex flex-column align-center">
    <div style="margin-top: 5%;"></div>
    <div class="logo">
      <span class="letter" data-letter="M">M</span>
      <span class="letter" data-letter="O">O</span>
      <span class="letter" data-letter="V">V</span>
      <span class="letter" data-letter="I">I</span>
      <span class="letter" data-letter="G">G</span>
      <span class="letter" data-letter="A">A</span>
      <span class="letter" data-letter="T">T</span>
      <span class="letter" data-letter="I">I</span>
      <span class="letter" data-letter="O">O</span>
      <span class="letter" data-letter="N">N</span>
    </div>
    <div style="margin-top: 5%;"></div>
    <h1 class="slogan">Find Your Best Movie</h1>
    <h1>당신의 영화 길잡이</h1>
    <div class="tech-slideshow">
      <div class="mover-1"></div>
      <v-img src="@/assets/panorama-sample.jpg"/>
    </div>
  </v-container>
</template>

<script>

  export default {
    name: 'HomeView',
    components: {
    },
  }
</script>

<style>

  @import url(https://fonts.googleapis.com/css?family=Lato:900);

  *, *:before, *:after{
    box-sizing:border-box;
  }
  body{
    font-family: 'Lato', sans-serif;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
    user-select:none;

  }
  div.logo{
    width: 90%;
    margin: 0 auto;
    text-align: center;
  }
  .letter{
    display: inline-block;
    font-weight: 900;
    font-size: 8em;
    margin: 0.08em;
    position: relative;
    color: #00B4F1;
    transform-style: preserve-3d;
    perspective: 400;
    z-index: 1;
  }
  .letter:before, .letter:after{
    position:absolute;
    content: attr(data-letter);
    transform-origin: top left;
    top:0;
    left:0;
  }
  .letter, .letter:before, .letter:after{
    transition: all 0.3s ease-in-out;
  }
  .letter:before{
    color: black;
    text-shadow: 
      -1px 0px 1px rgba(255,255,255,.8),
      1px 0px 1px rgba(0,0,0,.8);
    z-index: 3;
    transform:
      rotateX(0deg)
      rotateY(-5deg)
      rotateZ(0deg);
  }
  .letter:after{
    color: rgba(0,0,0,.11);
    z-index:2;
    transform:
      scale(1.08,1)
      rotateX(0deg)
      rotateY(0deg)
      rotateZ(0deg)
      skew(0deg,1deg);
  }

  .logo:hover .letter:before{
    color: #202020;
    transform:
      rotateX(0deg)
      rotateY(-30deg)
      rotateZ(0deg);
  }
  .logo:hover .letter:after{
    transform:
      scale(1.08,1)
      rotateX(0deg)
      rotateY(40deg)
      rotateZ(0deg)
      skew(0deg,11deg);
  }
  .slogan {
    font-size: 5em;
    color: #00B4F1;
  }

.tech-slideshow {
  height: 200px;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
  transform: translate3d(0, 0, 0);
}

.tech-slideshow > div {
  height: 200px;
  width: 2526px;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  transform: translate3d(0, 0, 0);
}
.tech-slideshow .mover-1 {
  animation: moveSlideshow 12s linear infinite;
}
.tech-slideshow .mover-2 {
  opacity: 0;
  transition: opacity 0.5s ease-out;
  background-position: 0 -200px;
  animation: moveSlideshow 15s linear infinite;
}
.tech-slideshow:hover .mover-2 {
  opacity: 1;
}

@keyframes moveSlideshow {
  100% { 
    transform: translateX(-66.6666%);  
  }
}

</style>
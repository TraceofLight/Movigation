<template>
  <v-container class="d-flex flex-column align-center">
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
    <h1 class="slogan">Find Your Best Movie</h1>
    <div style="margin-top: 5%;"/>

    <section class="carousel">

    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="carousel__wrapper">

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/1/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/2/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/3/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/4/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/5/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/6/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/7/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/8/200/300');"></div>
            </div>

            <!--#### repeat ####-->
            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/1/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/2/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/3/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/4/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/5/200/300');"></div>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/6/200/300');"/>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/7/200/300');"/>
            </div>

            <div class="carousel__slide">
              <div class="carousel__image" style="background-image: url('https://picsum.photos/seed/8/200/300');"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
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

/* carousel */

:root {
  --no-of-slides: 8;
  --slides-in-view: 6;
  --slide-width: 200px;
  --slide-height: 300px;
  --iteration-time: 10s;
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(var(--slide-width) * var(--no-of-slides)* -1));
  }
}

.carousel__wrapper {
  display:flex;

  /*justify-content: center;*/
  align-items: center;
  
  width: 100vw;
  overflow: hidden;
  margin: 0 auto;
}

.carousel {
  overflow: hidden;
}

.carousel__slide {
  animation: scroll var(--iteration-time) linear infinite;
  display: flex;
  flex-direction: column;
  
  flex: 0 0 auto;
  width: var(--slide-width);
  height: var(--slide-height);
  box-sizing: border-box;
  /*border: 1px dotted darkblue;*/
}

.carousel__image {
  background-size: cover;
  background-repeat: no-repeat;
  
  height: 100%;
}

/* just for analysis remove this 3 rules later*/
.carousel__slide {
  position: relative;
}

.carousel__slide::before {
  position: absolute;
  top: 0%;
  left: 50%;
  font-size: 2rem;
  color: lime;
}

</style>
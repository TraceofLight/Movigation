<template>
  <section class="section carousel">
      <div class="container">
          <div class="row">
              <div class="col-xs-12">
                  <h2 class="section__title"><strong></strong> TOP Featured<code-pen id="yrQyBj"></code-pen>
                  </h2>
                  <p class="section__description">Find Your Best Movie</p>
              </div>
          </div>
          <div class="row">
              <div class="col-xs-12">
                  <agile class="main" ref="main" :options="option1" :as-nav-for="asNavFor1">
                      <div class="slide" 
                      v-for="(slide, index) in slides" 
                      :key="index" 
                      :class="`slide--${index}`">
                        <img :src="slide" />
                      </div>
                  </agile>
              </div>
              <div class="col-xs-12">
                  <agile class="thumbnails"
                        ref="thumbnails" 
                        :options="option2" 
                        :as-nav-for="asNavFor2">
                    <div class="slide slide--thumbnail" 
                            v-for="(slide, index) in slides" 
                            :key="index" 
                            :class="`slide--${index}`" 
                            @click="$refs.thumbnails.goTo(index)">
                      <img :src="slide" />
                    </div>
                  </agile>
              </div>
          </div>
      </div>
  </section>
</template>

<script>
  export default {
    name: 'MovieCarousel',
    data () {
      return {
        asNavFor1: [],
        asNavFor2: [],
        option1: {
          dots: false,
          fade: true,
          navButtons: false
        },
        option2: {
          autoplay: true,
          autoplaySpeed: 5000,
          centerMode: true,
          dots: false,
          navButtons: false,
          slidesToShow: 5,
          // responsive: [
          //   {
          //     breakpoint: 600,
          //     settings: {
          //       slidesToShow: 5
          //     }
          //   },
          //   {
          //     breakpoint: 1000,
          //     settings: {
          //       navButtons: true
          //     }
          //   }
          // ]
        },
        slides: [
          'https://images.unsplash.com/photo-1453831362806-3d5577f014a4?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
          'https://images.unsplash.com/photo-1496412705862-e0088f16f791?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
          'https://images.unsplash.com/photo-1506354666786-959d6d497f1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
          'https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
          'https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
          'https://images.unsplash.com/photo-1472926373053-51b220987527?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
          'https://images.unsplash.com/photo-1497534547324-0ebb3f052e88?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ'
        ]
      }
    },
    mounted () {
      this.asNavFor1.push(this.$refs.thumbnails)
      this.asNavFor2.push(this.$refs.main)
    }
  }
</script>

<style>
.carousel .main {
  margin-bottom: 30px; }

.carousel .thumbnails {
  margin: 0 -5px;
  width: calc(100% + 10px); }

.carousel .agile__actions {
  position: static; }

.carousel .agile__nav-button {
  background: transparent;
  border: none;
  color: #ccc;
  cursor: pointer;
  font-size: 24px;
  transition-duration: .3s; }
  .carousel .agile__nav-button:hover {
    color: #888; }

.carousel .agile__dot {
  margin: 0 10px; }
  .carousel .agile__dot button {
    background-color: #eee;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: block;
    height: 10px;
    font-size: 0;
    line-height: 0;
    margin: 0;
    padding: 0;
    transition-duration: .3s;
    width: 10px; }
  .carousel .agile__dot--current button, .carousel .agile__dot:hover button {
    background-color: #888; }

.carousel .thumbnails .agile__nav-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%); }
  .carousel .thumbnails .agile__nav-button--prev {
    left: -45px; }
  .carousel .thumbnails .agile__nav-button--next {
    right: -45px; }

.carousel .slide {
  align-items: center;
  box-sizing: border-box;
  color: #fff;
  display: flex;
  height: 450px;
  overflow: hidden;
  justify-content: center; }
  .carousel .slide--thumbnail {
    cursor: pointer;
    height: 100px;
    padding: 0 5px;
    transition: opacity .3s; }
    .carousel .slide--thumbnail:hover {
      opacity: .75; }
  .carousel .slide img {
    height: 100%;
    object-fit: cover;
    object-position: center;
    width: 100%; }

  .sub-carousel {
    max-width: 100%;
    overflow: hidden;
  }
</style>
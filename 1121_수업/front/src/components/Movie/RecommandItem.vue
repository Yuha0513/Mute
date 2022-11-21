<template>
  <div class="reco_box">
    {{recommand.title}}
  </div>
</template>

<script>
export default {
    name: 'RecommandItem',
    props: {
        recommand: Object,
    },
    data() {
      return {
        poster: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.recommand.poster_path }` 
      }
    }
}
</script>

<style>
.reco_box {
  width: 32%;
  height: auto;
  border: 1px solid #ccc;
  margin-right: 1%;
  background: white;
  border-radius: 10px;
  transition: 0.9;
}
.reco_box:hover{
    box-shadow: 0 0 11px rgba(33, 33, 33, 0.5);
    cursor: pointer;
}
</style>
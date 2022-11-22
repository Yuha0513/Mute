<template>
  <div>
    {{movie.title}}
  </div>
</template>

<script>
export default {
  name: 'LikeMovieItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>
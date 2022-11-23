<template>
  <div>
    <div class="genre_container">
      <ChartBase/>
    </div>
    <div>
      <RandomMovie/>
    </div>
  </div>
</template>

<script>
import ChartBase from '@/components/Genre/ChartBase'
import RandomMovie from '@/components/Genre/RandomMovie'

export default {
    name: 'GenreView',
    components: {
      ChartBase,
      RandomMovie
    }
}
</script>

<style>
.genre_container{
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
<template>
  <ul class="youtube_list">
    <YoutubeListItem
      v-for="(video, idx) in youtubeVideos"
      :key="idx"
      :video="video"
    />
  </ul>
</template>

<script>
import YoutubeListItem from '@/components/YoutubeListItem'

export default {
  name: 'YoutubeList',
  created() {
    this.$store.dispatch('getYoutube', this.movyoutube)
  },
  props: {
    movyoutube: { type : String, required: true }
  },
  computed: {
    youtubeVideos() {
      return this.$store.state.youtubeVideos
    }
  },
  components: {
    YoutubeListItem
  }
}
</script>

<style>
.youtube_list {
  display: flex;
  align-content: center;
  justify-content: center;
}
</style>
<template>
  <li>
    <!-- {{ video?.snippet.title}} -->
    <div class="youtube_video">
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
  </li>
</template>

<script>
export default {
  name: 'YoutubeListItem',
  data() {
    return {
      dialog: false
    }
  },
  props: {
    video: {
      type: Object,
      required: true,
    },
  },
  computed: {
    imgSrc() {
      return this.video.snippet.thumbnails.high.url
    },
    videoUrl() {
      const videoId = this.video?.id.videoId
      return `https://www.youtube.com/embed/${videoId}` 
    }
  }
}
</script>

<style>
.youtube-list-item {
  display: flex;
  margin-bottom: 1rem;
  cursor: pointer;
  transition: transform 500ms;
}
</style>
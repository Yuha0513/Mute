<template>
  <li>
    <!-- <v-dialog
      v-model="dialog"
      hide-overlay 
      width="1000px" 
    >
    <template v-slot:activator="{ on, attrs }"> 
      <img 
        :src="imgSrc" 
        alt="thmbnail"
        v-bind="attrs"
        v-on="on"
        >
    </template> -->
      <div>
        <!-- {{ video?.snippet.title}} -->
        <iframe :src="videoUrl" frameborder="0"></iframe>
      </div>

    <!-- </v-dialog> -->
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
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}` 
    }
  }
}
</script>

<style>

</style>
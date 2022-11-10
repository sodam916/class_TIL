<template>
  <div v-if="video">
    <h1>Detail</h1>
    <div>
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
    <div>
      {{ video?.snippet.title | stringUnescape}}
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape(rawText) {
      return _.unescape(rawText)
    }
  },
}
</script>

<style>

</style>
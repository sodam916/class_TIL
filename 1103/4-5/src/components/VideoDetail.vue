<template>
  <div>
    <div v-if="selectedVideo" class='ratio ratio-16x9'>
      <iframe :src="videoUrl" frameborder="0" ></iframe>
    </div>
    <div v-else>
      <p>선택한 비디오가 없습니다</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: Object,
  },
  computed: {
    videoUrl() {
      return `https://www.youtube.com/embed/${this.selectedVideo.id.videoId}`
    }
  }
}
</script>

<style>

</style>
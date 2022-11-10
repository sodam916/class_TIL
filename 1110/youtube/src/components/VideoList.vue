<template>
  <div>
    <ul class="list-group">
      <VideoListItem
        v-for="video in videos"
        :key="video.etag"
        :video="video"
        @choose-video="chooseVideo"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videos: Array,
  },
  methods: {
    chooseVideo(video) {
      // console.log('리스트', video.snippet.title)
      this.$emit('choose-video', video)
    }
  }
}
</script>

<style>

</style>
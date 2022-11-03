<template>
  <div>
    <ul class="list-group">
    <VideoListItem
      v-for="video in videos"
      :key="video.etag"
      :video="video"
      @select-video="selectVideo"
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
    selectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>
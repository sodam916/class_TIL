<template>
  <div>
    <li @click="selectVideo" class="list-group-item">
      <div class=''>
        <img :src="thumbnailUrl">
        {{ videoTitle }}
      </div>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoTitle() {
      return _.unescape(this.video.snippet.title)
    },
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    },
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>

</style>
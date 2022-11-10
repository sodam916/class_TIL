<template>
  <li class="list-group-item" @click="chooseVideo">
    <img :src="thumbnailUrl">
    <span>
      {{ videoTitle | stringUnescape }}
    </span>

  </li>
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
      return this.video.snippet.title
    },
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    },
  },
  filters: {
    stringUnescape(rawText) {
      return _.unescape(rawText)
    }
  },
  methods: {
    chooseVideo() {
      this.$emit('choose-video',this.video)
    }
  }
}
</script>

<style>

</style>
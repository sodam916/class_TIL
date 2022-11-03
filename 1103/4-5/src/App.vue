<template>
  <div id="app">
    <div class='container'>
      <h1>SSAFY TUBE</h1>
      <searchBar
        @input-change="inputChange"
      />
      <div class='row'>
        <div class="col-12 col-lg-8">
            <VideoDetail
              :selected-video="selectedVideo"
            />
        </div>
        <div class="col-12 col-lg-4">
          <VideoList
            :videos="videos"
            @select-video="selectVideo"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import searchBar from '@/components/searchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const my_api= process.env.VUE_APP_YOUTUBE_KEY
// console.log(my_api)

export default {
  name: 'App',
  data:function () {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  components: {
    searchBar,
    VideoList,
    VideoDetail

  },
  methods: {
    selectVideo: function (video) {
      this.selectedVideo = video
    },
    inputChange: function (query) {
      // console.log(query)
      axios({
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: my_api,
          part: 'snippet',
          q: query,
          type: 'video',

        }
      })
      .then(res => {
        this.videos = res.data.items
      })
    },
  }
}
</script>

<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

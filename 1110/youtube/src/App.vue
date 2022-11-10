<template>
  <div id="app">
    <header>
      <h1>Youtube Project</h1>
      <TheSearchBar
        @input-change="inputCahnge"
      />
    </header>
      <br>
    <section>
      <p>
        <VideoDetail :video="selectedVideo" />
      </p>
      <VideoList 
      :videos='videos'
      @choose-video="chooseVideo"
      />
    </section>

  </div>
</template>

<script>
import axios from 'axios'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import TheSearchBar from '@/components/TheSearchBar'


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// console.log(API_KEY)

export default {
  name: 'App',
  components: {
    VideoList,
    TheSearchBar,
    VideoDetail
  },
  data() {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    inputCahnge(query) {
      axios({
        url: 'https://www.googleapis.com/youtube/v3/search' ,
        method: 'get',
        params: {
          key: API_KEY,
          part: 'snippet',
          q: query, //검색어
          type: 'video',
        },
      })
      .then((res) => {
        // console.log(res)
        this.videos = res.data.items
      })
      .catch((err) => {
        console.log(err)
      })
    },
    chooseVideo(video) {
      // console.log(video.snippet.title)
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  position: relative;
  overflow: hidden;
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio (divide 9 by 16 = 0.5625) */
}

section {
  display: flex
}

p {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 100%;
}
</style>

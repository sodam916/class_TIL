<template>
  <div id="app">
    <div class="container">
      <h1>버튼 박스 제작</h1>
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div class="timebox">
        <a
          v-for="time in times" 
          :key ="time.index"
        >
          <button class="btn" @click="clickBtn">{{time}}</button>
        </a>
      </div>
    </div>
    <hr>
    <p> 선택시간 : 
    <span 
      v-for="(selecttime, index) in timeList" 
      :key="index" class="textt"
      >
      {{ selecttime }}
    </span>
    </p>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {

  },
  data: function () {
    return {
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
],
      number: 0,
      timeList: [],
    }
  },
  methods: {
    clickBtn(event) {
      if (event.target.classList.value === 'btn'){
        this.number += 1
        if (this.number > 5) {
          alert('5타임까지만 신청할 수 있습니다')
        } else {
          event.target.classList = 'selected'
          this.timeList.push(event.target.innerText)
        }
        console.log(this.timeList)
        console.log(event.key)
      } else if (event.target.classList.value === 'selected'){
        event.target.classList = 'btn'
        const index = this.timeList.indexOf(event.target)
        this.timeList.splice(index, 1)
        this.number -= 1
      }
    } 
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}
.container {
  align-items: center;
  justify-content: center;
  display: flex;
  flex-direction: column;
}

.btn {
  color: #84898C;
  align-content: center;
  justify-content: center;
  background-color: white;
  margin: 4px;
  border: none
}

.timebox {
  justify-content: center;
  align-content: flex;
  width: 500px;
  height: 150px;
}
.selected {
  color:#0F4C81;
  background-color: rgb(159, 209, 229);
  border: none;
  margin: 4px;
}
.textt {
  margin: 5px;
}
</style>

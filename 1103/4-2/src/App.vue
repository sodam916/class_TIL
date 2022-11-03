<template>
  <div id="app">
    <div class="parent">
      <div class='first'>
        <div>
          <h2>예약페이지</h2>
        </div>
        <div>
          <h4>선생님 선택</h4>
          <div v-for="teacher in teachers" :key="teacher.index">
            <button class="teacherbutton">{{ teacher }}</button>
          </div>
        </div>
        <div>
          <button></button>
        </div>
      </div>
      <div class='second'>
        <h2>상담 신청 현황</h2>
      </div>
    </div>

  </div>
</template>

<script>


export default {
  name: 'App',
  components: {

  },
  data: function () {
    return {
      teachers: ['Eric','Tony'],
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
],
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
  /* margin-top: 60px; */
}
.parent {
  width: 100%;
  display: flex;
}
.first {
  width:50%;
}
.second {

  width:50%;
  height: 500px;
  background-color: rgb(175, 214, 230);
}
.teacherbox {

}

.teacherbutton {
  border-color: #0F4C81;
  background-color: white;
  width: 80px;
  height: 40px;
  margin: 10px;
}
.selectedteacher {
  border-color: #0F4C81;
  background-color: #9cb7cf;
}
</style>

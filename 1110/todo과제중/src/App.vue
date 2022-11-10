<template>
  <div id="app">
    <div class="choicebox">
      <p><router-link :to="{ name: 'todoall'}">전체</router-link></p>
      <p><router-link :to="{ name: 'important'}">중요</router-link></p>
      <p><router-link :to="{ name: 'today'}">오늘</router-link></p>
    </div>
    <div class="viewbox">
      <router-view/>
    </div>
  </div>
</template>

<style>
#app {
  display: flex;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  justify-content: center;
  justify-content: space-around;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.choicebox {
  display: flex;
  flex-direction: column;
  border: solid 1px black;
  border-radius: 5px;
  width: 250px;
  
}

.viewbox {
  border: solid 1px black;
  width: 700px;
  height: 300px;
  border-radius: 5px;
}
</style>

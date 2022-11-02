<template>
  <div id="app">
    <h2>App</h2>
    <div>
      <input type="text">
      parentData : {{ parentdata }}
    </div>
    <AppParent @create-parent-data="createParentData"/>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function () {
    return {
      parentdata: '',
    }
  },
  methods: {
    createParentData: function (parentdata) {
      this.parentdata = parentdata 
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
}
</style>

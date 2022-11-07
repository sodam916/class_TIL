<template>
  <div id="app">
    <h1>Counter App</h1>
    <h3>Counter : {{ counter}}</h3>
    <h3>Counter x 2 : {{ doubleCounter }}</h3>
    <span>
      <button
        @click="increaseNumber"
      >increase + </button>
      <button
        @click="decreaseNumber"
      >decrease - </button>
    </span>
    
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {

  },
  computed: {
    counter() {
      return this.$store.state.counter
    },
    doubleCounter() {
      return this.$store.getters.doubleCounter
    }
    // doublecounter() {
    //   return this.counter * 2
    // }
  },
  methods: {
    increaseNumber() {
      // this.$store.state.counter++
      this.$store.dispatch('increaseNumber')
    },
    decreaseNumber() {
      this.$store.dispatch('decreaseNumber')
      // this.$store.state.counter--
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

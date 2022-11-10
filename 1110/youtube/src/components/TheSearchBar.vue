<template>
  <div>
    <input
      @keyup.enter="inputChange"
      type="text"
     >
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  data() {
    return {

    }
  },
  methods: {
    inputChange(event) {
      // console.log(event.target.value)
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>

</style>
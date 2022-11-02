<template>
  <div>
    <h2>AppChild</h2>
    <div>
      <input type="text"
      v-model="childData"
      @keyup.enter="createChildData"
      >
    </div>
  </div>
</template>

<script>
export default {
  name:'AppChild',
  data: function () {
    return {
      childData: null
    }
  },
  methods: {
    createChildData: function () {
      this.$emit('create-child-data', this.childData)
      this.childData = null
    }
  }
}
</script>

<style>

</style>
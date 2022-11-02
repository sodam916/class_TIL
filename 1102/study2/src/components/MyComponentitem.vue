<template>
  <div>
    <h3>컴포넌트의 하위차일드</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭</button>
    <input 
    type="text" 
    v-model="childInputData"
    @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name: 'MyComponentitem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childToParent: function () {
      this.$emit('give-me-money', 100)
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = null
    }
  },
}
</script>

<style>

</style>
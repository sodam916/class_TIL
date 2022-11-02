<template>
  <div>
    <h2>AppParent</h2>
    <div>
      <input type="text"
      v-model="parentData"
      @keyup.enter="createParentData"
      >
      childData: {{ childData }}
    </div>
    <AppChild @create-child-data="createChildData"/>

  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  data: function () {
    return {
      childData: '',
      parentData: '',
    }
  },
  methods: {
    createChildData: function (childdata) {
      this.childData = childdata
    },
    createParentData: function () {
      this.$emit('create-parent-data',this.parentData)
      this.parentData = null
    }
  }
}
</script>

<style>

</style>
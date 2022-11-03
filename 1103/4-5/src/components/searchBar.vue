<template>
  <div>
    <input type="text"
    v-model.trim="query"
    @keyup.enter="onInputChange"
    >
    <button class="btn btn-primary">검색</button>
  </div>
</template>

<script>
export default {
  name: 'searchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    onInputChange : function () {
      if(!this.query) {
        alert('내용이 없습니다')
      }
      this.$emit('input-change', this.query)
    }
  }
}
</script>

<style>

</style>
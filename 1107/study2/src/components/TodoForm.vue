<template>
  <div>
    <input type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
  </div>
</template>

<script>

export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      if (this.todoTitle) {
        this.$store.dispatch('createTodo',this.todoTitle)
      } else {
        alert('내용이 없습니다')
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>
<template>
  <div id="app">
    <h1>TodoList</h1>
    <h3>모든 Todo 개수 {{ allTodosCount }}</h3>
    <h3>끝낸 할일 {{ completedTodosCount }}</h3>
    <h3>아직 {{ unCompletedTodosCount }}</h3>
    <TodoList/>
    <TodoForm/>
    <!-- <button @click="loadTodos">불러오기</button> -->
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm
  },
  computed: {
    allTodosCount() {
      return this.$store.getters.allTodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    unCompletedTodosCount() {
      return this.$store.getters.unCompletedTodosCount
    }
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
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

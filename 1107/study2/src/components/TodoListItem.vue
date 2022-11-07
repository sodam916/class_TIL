<template>
  <div>
    <h5>
      <span
        @click="updateTodoStatus"
        :class="{'is-completed': todo.isCompleted}"
      >
        {{todo.title}}
        <button
          @click="deleteTodo"
        >delete</button>
      </span>
    </h5>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
      //context.commit('DELETE_TODO', todoItem) 여기서 해도 가능
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
      // console.log(this.todo)
      // this.todo.classList = 'is-completed'
    }
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
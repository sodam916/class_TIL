<template>
  <div>
    <h3>Todo</h3>
    <div 
    v-for="onetodo in list"
    :key="onetodo.id">
    {{onetodo.content}}
    </div>
  </div>
</template>

<script>
// import todo from '@/store/modules/todo.js'
import { mapState } from 'vuex';

export default {
  name: 'AllTodoPage',
  computed: {
    ...mapState('todo', {
      list: state => state.list
    })
    }
  }

</script>

<style>

</style>
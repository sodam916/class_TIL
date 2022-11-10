import Vue from 'vue'
import Vuex from 'vuex'
import todo from '@/store/modules/todo.js'
Vue.use(Vuex)

export default new Vuex.Store({
  
  modules: {
    todo
  },
  state: {
    // ...todo(['list',])
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
})

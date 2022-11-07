import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    doubleCounter(state) {
      return state.counter * 2
    }
  },
  mutations: {
    INCREASE_NUM(state) {
      state.counter++
    },
    DECREASE_NUMBER(state) {
      state.counter--
    }
  },
  actions: {
    increaseNumber(context) {
      context.commit('INCREASE_NUM')
    },
    decreaseNumber(context) {
      context.commit('DECREASE_NUMBER')
    }
  },
  modules: {
  }
})

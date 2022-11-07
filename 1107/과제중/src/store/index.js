import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
    {
      title: '아메리카노',
      price: 3000,
      selected: true,
      image: '<https:source.unsplash.com/featured/?americano>'
    },
    {
      title: '카페라떼',
      price: 4000,
      selected: true,
      image: '<https:source.unsplash.com/featured/?cafelatte>'
    },
    {
      title: '오렌지쥬스',
      price: 3500,
      selected: true,
      image: '<https:source.unsplash.com/featured/?orangejuice>'
    }
  ],
    sizeList: [
    {
      name: 'small',
      price: 500,
      selected: true,
    },
    {
      name: 'midium',
      price: 1000,
      selected: true,
    },
    {
      name: 'large',
      price: 2000,
      selected: true,
    },

  ],
  },
  getters: {
  },
  mutations: {
    addOrder(state) {
      state.menuList.forEach((menu) => {
        if (menu.selected === true) {
          state.orderList.push(menu)
        }
      })
      state.sizeList.forEach((size) => {
        if (size.selected === true) {
          state.orderList.push(size)
        }
      })
    },
    updateMenuList(state, selectedMenu) {
      state.menuList.forEach((menu) => {
        if (menu === selectedMenu) {
          menu.selected = true
          state.orderList.push(menu)
        }
      })
    },
    updateSizeList(state, selectedSize) {
      state.sizeList.forEach((size) => {
        if (size === selectedSize) {
          size.selected = true
          state.orderList.push(size)
        }
      })
    },
    SELECTED_MENU(state, selectMenu) {
      selectMenu.selected = !selectMenu.selected
      
      
    }
  },
  actions: {
    selectedMenu(context,selectMenu) {
      context.commit('SELECTED_MENU',selectMenu)
    }
  },
  modules: {
  }
})
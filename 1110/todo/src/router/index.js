import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPage from '../views/AllTodoPage'
import TodayTodoPage from '../views/TodayTodoPage'
import ImportantTodoPage from '../views/ImportantTodoPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/all',
    name: 'todoall',
    component: AllTodoPage
  },
  {
    path: '/important',
    name: 'important',
    component: ImportantTodoPage
  },
  {
    path: '/today',
    name: 'today',
    component: TodayTodoPage
  }
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

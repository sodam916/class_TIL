<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <MenuList/>
    <OrderList/>
 </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import OrderList from '@/components/OrderList'

export default {
  name: 'App',
  components: {
    MenuList,
    OrderList
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  text-align: center;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>

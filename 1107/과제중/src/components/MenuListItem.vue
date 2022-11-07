<template>
  <div class="box"
    @click="selectedMenu">
    
      <img :src= "menu.image" width="10px">
      {{ menu.title }}
      {{ menu.price }}
    
    
    
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    selectedMenu(event) {
      this.$store.dispatch('selectedMenu', this.menu)
      event.target.classList = 'is-selected'
    }
  }
}
</script>

<style>
  .box {
    display: flex;
    border: solid 1px black;
    width: 400px;
    height: 50px;
    border-radius: 10px;
    margin-bottom: 5px;
    justify-content: space-around;
    
  }
  .is-selected {
    border: solid 1px black;
    width: 400px;
    height: 50px;
    border-radius: 10px;
    margin-bottom: 5px;
    background-color: green;
  }
</style>
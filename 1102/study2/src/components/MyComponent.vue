<template>
  <div class="border">
    <h1>새로운 컴포넌트</h1>
    <MyComponentitem static-props="My Component에서 보낸 데이터"
    :dynamic-props="dynamicProps"
    @give-me-money="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyComponentitem from '@/components/MyComponentitem'

export default {
  name: 'MyComponent',
  data: function () {
    return {
      dynamicProps: '동적데이터 보내는중,,',
    }
  },
  components: {
    MyComponentitem,
  },
  methods: {
    parentGetEvent: function (childData) {
      if (childData > 0) {
        childData -= 10
        console.log(childData)
      }
    },
    getDynamicData: function (dynamicdata) {
      console.log(`사용자 입력값${dynamicdata}입니다`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>
// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log(i)
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.


/*
const 를 let 으로 바꾼다
const의 경우 일기 전용 상수를 선언해주는 것이기 때문
*/

// 2번


for (const num of nums) {
  console.log(num, typeof num)
}

/* 
in 을 of로 변경
in 의 경우 속성을 순회할 때 사용
of 의 경우 객체를 순회할 때 사용
 */

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

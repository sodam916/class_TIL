// 함수정의

function myFunc(arg1, arg2, ...arg3) {

  console.log(arg1, arg2, arg3)
}

myFunc(1, 2, 3, 4)   // 1 2 [ 3, 4 ]

arr1 = [1, 2, 3, 4, 5]
myFunc(...arr1) // ... 을 인자로 주면 풀어서 호출한것과 같음  결과 > 1 2 [ 3, 4, 5 ]

arr2 = ['a', 'b',...arr1, 'c',]

console.log(arr2)
/* 
[
  'a', 'b', 1, 2,
  3,   4,   5, 'c'
]
 */



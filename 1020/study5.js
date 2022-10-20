arr = [1, 2, 3, 4, 5]

// elem : 개별 요소  idx : 요소의 인덱스  arr : 배열
const arrFunc = function (elem, idx, arr) {
  console.log(elem, idx, arr)
}

arr.forEach(arrFunc)
/* 
1 0 [ 1, 2, 3, 4, 5 ]
2 1 [ 1, 2, 3, 4, 5 ]
3 2 [ 1, 2, 3, 4, 5 ]
4 3 [ 1, 2, 3, 4, 5 ]
5 4 [ 1, 2, 3, 4, 5 ]
*/

arr.forEach((elem, idx) => {
  console.log(elem, idx)
})

/*
1 0
2 1
3 2
4 3
5 4
*/


let result = arr.map((elem) => {
  return elem**3
})
console.log(result)
// [ 1, 8, 27, 64, 125 ]


result = arr.filter((elem) =>{
  return elem %2
})
console.log(result)  // [ 1, 3, 5 ]


result = arr.filter((elem) => {
  return elem % 2
}).map((elem) => {
  return elem**3
})
console.log(result)   //[ 1, 27, 125 ]
// 화살표함수 (익명함수)

//함수 선언식
function functionName(name) {

}

//함수 표현식
const functionVar = function (name) {

}

const add = function (a, b) {
  return a + b
}

function func(f) {
  console.log(f(1, 2))
}

func(add)
func( function (a, b) {
  return a + b
})



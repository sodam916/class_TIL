function func(f) {
  console.log(f(1, 2))
}

// (a, b) => {
//   return a+b
// }

/* 
매개변수가 하나면 괄호도 생략 가능 
return문 하나면 중괄호 생략 가능
return도 생략 
*/
(a, b) => { return a + b }

(a, b) => a + b

func((a, b) => a + b)


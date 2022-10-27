function asyncFunc() {
  const result = new Promise(function (resolve, reject) {     // Promise 는 클래스 / 클래스는 앞에 new 붙여서 부름
    const now = new Date()
    if(now.setSeconds() % 2 != 0) {
      resolve('성공')
    } else {
      reject('실패')
    }
    // 일을 처리한 뒤 
    // resolve('성공')
    // reject('실패')
  })
  return result
}


asyncFunc()
  // 성공한 경우 실행할 코드
  .then(function(success) {  
    console.log(success)
    return 100
  })
  .then(res => console.log(res))
  .then(res => console.log(res))
  // 실패한 경우 실행 코드
  .catch(fail => console.log(fail))   
  .finally(() => console.log('final'))
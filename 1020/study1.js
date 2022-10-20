color = 'red'    

switch(color) {
  case 'red':
    console.log(0)
    break
  case 'blue':
    console.log(1)
    break
  case 'green':
    console.log(2)
    break
  case 'yellow':
    console.log(3)
    break
  default: // 외의 경우
    console.log(10)
}
/* 
num이 뭐냐에 따라 조건을 나눠서 시작점을 설정 가능 
*/

score = 82

if(score > 90){
  console.log('excellent')
} else if(score > 80){
  console.log('good')
} else if(score > 70){
  console.log('nice')
} else { // == default
  console.log('again')
}

/* switch의 경우 조건을 범위내에서 찾는것은 힘듦 */
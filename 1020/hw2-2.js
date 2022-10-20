let star = ''

for(let i=0; i < 9; i += 2) {
  star += ' '.repeat((9-i)/2)
  star += '*' 
  console.log(star)
}
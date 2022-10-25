let countA = 0
let countB = 0
const CA = document.querySelector('#countA')
const CB = document.querySelector('#countB')
const Computer = _.sample(['rock', 'scissors', 'paper'])
const P1 = document.querySelector('#player1-img')
let P2 = document.querySelector('#player2-img')
const aaa = (['rock', 'scissors', 'paper'])
[주소1, 주소2, 주소3]
const tmp = -1
tmp ++
img = document.getElementById()
img.src = arr[tmp % 3]

setInterval(함수, 100)
var Presult = 'scissors'
const playGame = (p1_choice, p2_choice) => {
	switch(p1_choice) {
		case 'rock':{
      console.log('동작중')
			if (p2_choice === 'rock') {
				
			}
			else if (p2_choice === 'scissors') {
        console.log('동작중')
				countA += 1
			}
			else if (p2_choice === 'paper') {
        console.log('동작중')
				countB += 1
			}
		}
    
		break
		case 'scissors' : {
			if (p2_choice === 'rock') {
				countB += 1
			}
			else if (p2_choice === 'scissors') {
				
			}
			else if (p2_choice === 'paper') {
				countA += 1
			}
		}
		break
		case 'paper' : {
			if (p2_choice === 'rock') {
				countA += 1
			}
			else if (p2_choice === 'scissors') {
				countB += 1
			}
			else if (p2_choice === 'paper') {
				
		}
	}
}}

function dis() {
  Rock.setAttribute('disabled', 'disabled')
  Scissors.setAttribute('disabled', 'disabled')
  Paper.setAttribute('disabled', 'disabled')
}

function change() {
  
}

const Scissors = document.querySelector('#scissors-button')
const Rock = document.querySelector('#rock-button')
const Paper = document.querySelector('#paper-button')



Scissors.addEventListener('click', function (event) {
  Presult = 'scissors'
  P1.src = `./img/${Presult}.png`
  P2.src = `./img/${Computer}.png`
  dis()
  playGame(Presult, Computer)
})

Rock.addEventListener('click', function (event) {
  Presult = 'rock'
  P1.src = `./img/${Presult}.png`
  P2.src = `./img/${Computer}.png`
  dis()
  playGame(Presult, Computer)
})

Paper.addEventListener('click', function (event) {
  Presult = 'paper'
  P1.src = `./img/${Presult}.png`
  P2.src = `./img/${Computer}.png`
  dis()
  playGame(Presult, Computer)
})
// console.log(Presult)

// CA.innerText = countA
// CB.innerText = countB


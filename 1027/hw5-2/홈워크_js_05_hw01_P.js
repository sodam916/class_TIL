axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response.data)
})

/*
동기란 모든 일을 순서대로 하나씩 처리하는 것이다
여기서 순서대로 란 이전 작업이 마무리되어야 다음 작업이 시작됨을 뜻한다

비동기란 작업 결과를 기다리지 않고 다음 작업을 처리하는 것을 말한다.
시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리하는 방식이다.
*/
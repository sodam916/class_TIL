<p style="font-size: 33px; font-weight: 700; margin-bottom: 3rem">Python 기초 II</p>

# 형변환(Type conversion, Typecasting)

파이썬에서 데이터타입은 서로 변환할 수 있습니다.

- 암시적 형변환
- 명시적 형변환

## 암시적 형변환(Implicit Typecasting)

사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우입니다. 아래의 상황에서만 가능합니다.

- bool
- Numeric Type (int, float, complex)


```python
# boolean과 integer는 더할 수 있을까요?
# True와 임의의 정수를 더해봅시다.
```


```python
True + 3  #더하기 가능
```


```python
# int, float, complex를 각각 변수에 대입해봅시다.
# 변수 int_number 에 정수를 할당해봅시다.
# 변수 float_numbe 에 실수를 할당해봅시다.
```


```python
int = 5
float = 7
complex = 9
int_number = 4
float_number = 2.5

```


```python
# int와 float를 더해봅시다. 그리고 값을 출력해봅시다.
# 그 결과의 type은 무엇일까요?
```


```python
print(int + float)
print(type(int + float))
```


```python
# int와 complex를 더해봅시다. 그리고 값을 출력해봅시다.
# 그 결과의 type은 무엇일까요?
```


```python
print(int + complex)
print(type((int + complex)))
```

## 명시적 형변환(Explicit Typecasting)

위의 상황을 제외하고는 모두 명시적으로 형변환을 해주어야합니다.

- string -> intger : 형식에 맞는 숫자만 가능
- integer -> string : 모두 가능

암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능합니다.

- `int()` : string, float를 int로 변환
- `float()` : string, int를 float로 변환
- `str()` : int, float, list, tuple, dictionary를 문자열로 변환


```python
# integer와 string 사이의 관계는 명시적으로 형변환을 해줘야만 합니다.
# 정수와 문자열을 더해보고 오류를 확인해봅시다.
```


```python
print(5 + 'hello')
```


```python
# 정수를 문자열로 형변환하고 문자열과 더해봅시다.
```


```python
print('5' + 'hello')
```


```python
# 변수 a에 string 3을 할당하고 integer로 변환해봅시다.
```


```python
a = str(3)
print(int(a))
```

    3
    


```python
# 변수 a에 string 3.5를 할당하고 float로 변환해봅시다.
```


```python
a = str(3.5)
print(float(a))
```

    3.5
    


```python
# string은 글자가 숫자일때만 형변환이 가능합니다.
# 변수 a에 문자열 'hi'를 할당하고 integer로 변환해봅시다.
```


```python
a = 'hi'
print(int(a))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [4], in <cell line: 2>()
          1 a = 'hi'
    ----> 2 print(int(a))
    

    ValueError: invalid literal for int() with base 10: 'hi'



```python
# string 3.5를 int로 변환할 수는 없습니다.
# 변수 a에 string 3.5를 저장하고 integer로 변환하고 오류를 확인해봅시다.
```


```python
a = str(3.5)
print(int(a))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [5], in <cell line: 2>()
          1 a = str(3.5)
    ----> 2 print(int(a))
    

    ValueError: invalid literal for int() with base 10: '3.5'



```python
# float 3.5는 int로 변환이 가능합니다.
# 변수 a에 실수 3.5를 저장하고 integer로 변환해봅시다.
```


```python
a = 3.5
print(int(a))
```

    3
    

## 컨테이너형 형변환

파이썬에서 컨테이너는 서로 변환할 수 있습니다.

<img width="708" alt="typecasting" src="https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png">



```python
# 하나의 결과를 확인 한 후, 주석 `#` 을 활용하여 이전의 코드를 비활성화 합니다.
# 형변환 후의 결과를 확인 합니다.
```


```python
# list를 형변환 해봅시다.
```


```python
l = [1, 2, 3, 4]
#str(l)
#tuple(l)
#set(l)
# range(l)
# dict(l)
```


```python
# tuple을 형변환 해봅시다.
```


```python
t = (1, 2, 3, 4)
#str(t)
#list(t)
#set(t)
#range(t)
#dict(t)
```


```python
# range를 형변환 해봅시다.
```


```python
r = range(1, 5)
#str(r)
#list(r)
#set(r)
#tuple(r)
# dict(r)
```


```python
# set을 형변환 해봅시다.
```


```python
s = {1, 2, 3, 4}
#str(s)
#list(s)
#tuple(s)
#range(s)
# dict(s)
```


```python
# dictionary를 형변환 해봅시다.
```


```python
d = {'name': 'ssafy', 'year': 2020}
#str(d)
#list(d)
#tuple(d)
#set(d)
# range(d)
```

# 정리
## 컨테이너(Container)
<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>

# 정리
## 컨테이너(Container)
<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>

# 연산자(Operator)

- 산술 연산자(Arithmetic Operator)
- 비교 연산자(Comparison Operator)
- 논리 연산자(Logical Operator)
- 복합 연산자(In-place Operator)
- 멤버십 연산자(Membership Operator)
- 식별 연산자(Identity Operator)
- 기타 (Indexing/Slicing)

## 산술 연산자 (Arithmetic Operator)
Python에서는 기본적인 사칙연산이 가능합니다. 

|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|

- 나눗셈 (`/`) 은 항상 float를 돌려줍니다.
- 정수 나눗셈 으로 (소수부 없이) 정수 결과를 얻으려면 `//` 연산자를 사용합니다.



```python
# 2의 1000승을 확인해봅시다.
```


```python
print(2**1000)
```

    10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
    


```python
# 나눗셈과 관련된 산술연산자를 활용해봅시다.
# 5와 2를 나눈 값을 출력해봅시다.
# 5와 2를 나눈 값의 몫을 출력해봅시다.
# 5와 2를 나눈 값을 integer로 형변환해봅시다.
# 5와 2를 나눈 값의 나머지를 출력해봅시다.
```


```python
print(5/2)
print(5//2)
print(int(5/2))
print((5/2) - 5//2)
```

    2.5
    2
    2
    0.5
    


```python
# divmod는 나눗셈과 관련된 함수입니다.
# divmode() 에 5와 2를 넣고 결과를 print로 확인해봅시다.
# 변수 quotient, remainder 에 divmode(5, 2)의 값을 할당해봅시다.
# f-string을 활용하여 quorient와 remainder의 값을 출력해봅시다.
```


```python
print(divmod(5, 2)) #몫과 나머지를 가져오는 함수
```

    (2, 1)
    


```python
# 음수 양수 표현도 해봅시다.
# 변수 positive_num 에 4를 할당하고 print할 때 -를 붙여서 print로 출력해봅시다.
# 변수 negative_num 에 -4를 할당하고 print할 때 + 와 - 를 붙여서 각각을 print로 출력해봅시다.
```


```python
positive_num = 4
print(- + positive_num)
negative_num = -4
print(+ + negative_num)
print(- + positive_num)
```

    -4
    -4
    -4
    

## 비교 연산자 (Comparison Operator)

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|객체 아이덴티티가 아닌경우|



```python
# 숫자의 대소관계를 비교해봅시다.
# 아무 정수 2개를 비교해봅시다.
```


```python
print(5 > 10)
```

    False
    


```python
# 다른 숫자인지 확인해봅시다.
# 3의 정수형과 실수형이 같은지 비교해봅시다.
```


```python
print(3 == 3.0)
```

    True
    


```python
# 같은 숫자인지 확인해봅시다.
# 같은 숫자를 != 를 확인하여 비교해봅시다.
```


```python
print(3 != 3.0)
```

    False
    


```python
# 문자열도 같은지 확인해봅시다.
# 대문자 HI와 소문자 hi가 같은지 확인해 봅시다.
```


```python
print('Hi' == 'hi')
print('Hi' != 'hi')
```

    False
    True
    


```python
# 특정 변수가 비어있는지 확인하기 위해서는
# x == None이 아닌 x is None을 쓰는 것을 권장합니다.
# 상세한 내용은 OOP 챕터에서 확인해 봅시다.
x = 3
x is None
```




    False



## 논리 연산자

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

다른 언어에서 논리연산자로 주로 사용하는 `&` 과 `|`은 파이썬에서 비트 연산자입니다.


```python
# and과 관련해서 모든 경우를 출력해봅시다.
# True와 False를 이용하여 and 의 모든 경우의 수(4개)를 출력해봅시다. 
# (True and True), (True and False), ...
```


```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

    True
    False
    False
    False
    


```python
# or과 관련해서 모든 경우를 출력해봅시다.
# True와 False를 이용하여 or 의 모든 경우의 수(4개)를 출력해봅시다.
# (True or True), (True or False), ...
```


```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

    True
    True
    True
    False
    


```python
# not을 활용해봅시다.
# print를 이용하여 True 와 0의 not 값을 각각 확인해봅시다.
```


```python
print(not True)
print(not 0)
```

    False
    True
    

* 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴합니다.
* 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴합니다.

논리연산자는 비교연산자와 함께 사용 가능합니다.


```python
num = 100
num >= 100 and num % 3 == 1
```

### 단축평가
* 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않습니다.
* 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도가 향상됩니다.


```python
# 문자열 'a'와 'b'의 and 값이 무엇인지 확인해봅시다.
```


```python
print('a' and 'b')
```

    b
    


```python
# 문자열 'a'와 'b'의 or 값이 무엇인지 확인해봅시다.
```


```python
print('a' or 'b')
```

    a
    


```python
vowels = 'aeiou'
```


```python
# 'a' and 'b' 의 결과값이 vowels에 포함이 되었는지 확인해봅시다.
```


```python
X
```


```python
# 'b' and 'a' 의 결과값이 vowels에 포함이 되었는지 확인해봅시다. 
```


```python
O
```

- `and` 는 둘 다 `True`일 경우만 `True`이기 때문에 첫 번째 값이 `True`라도 두번째 값을 확인해야 하기 때문에 `'b'`가 반환됩니다.
- `or` 는 하나만 `True`라도 `True`이기 때문에 `True`를 만나면 해당 값을 바로 반환합니다.


```python
# and의 단축평가(short-circuit evaluation)에 대해서 알아봅시다.
# (3 and 5) , (3 and 0), (0 and 3), (0 and 0) 의 결과를 print로 출력해봅시다.
```


```python
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)
```

    5
    0
    0
    0
    


```python
# or의 단축평가(short-circuit evaluation)에 대해서 알아봅시다.
# (3 or 5) , (3 or 0), (0 or 3), (0 or 0) 의 결과를 print로 출력해봅시다.
```


```python
print(5 or 3)
print(3 or 0)
print(0 or 3)
print(0 or 0)
```

    5
    3
    3
    0
    

## 복합 연산자

복합 연산자는 연산과 할당이 함께 이뤄집니다. 

반복문을 통해서 갯수를 카운트할 때 자주 사용합니다.

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|


```python
# 복합연산자는 사용 예시

# 0으로 할당된 변수 cnt 를
# 반복문 while 을 이용하여 5회 반복하는데
# 반복하는 동안 cnt를 print로 출력하고 cnt에 1씩 더해봅시다.
# 단, cnt 를 더할때는 복합연산자를 사용해봅시다.
```


```python
cnt = 0
while cnt < 5:
    print(cnt)
    cnt += 1
```

    0
    1
    2
    3
    4
    

## 식별 연산자 (Identity Operator)

`is` 연산자를 통해 동일한 object인지 확인할 수 있습니다. 

(OOP 챕터에서 다시 학습합니다.)


```python
# 파이썬에서 -5 부터 256 까지의 id는 동일합니다.
# 변수 a에는 3을 변수 b에는 3을 할당해봅시다.
# a 와 b 가 동일한 object인지 is 연산자를 통해 확인해봅시다.
# 그리고 a와 b의 id 값을 각각 출력해 봅시다.
```


```python
a = 3
b = 3
print(a is b)
print(id(a))
print(id(b))
```

    True
    2074684647792
    2074684647792
    


```python
# 257 이후의 id 는 다릅니다.
# 변수 a에는 257을 변수 b에는 257을 할당해봅시다.
# a 와 b 가 동일한 object인지 is 연산자를 통해 확인해봅시다.
# 그리고 a와 b의 id 값을 각각 출력해 봅시다.
```


```python
a = 257
b = 257
print(a is b)
print(id(a))
print(id(b))
```

    False
    2074794890160
    2074794890352
    

## 멤버십 연산자 (Membership Operatoe)

요소가 시퀀스에 속해있는지 확인할 수 있습니다.
- `in` 연산자
- `not in` 연산자


```python
# 리스트안에 특정한 정수가 있는지 확인해봅시다.
# 정수 1 이 [3, 2] 리스트에 속해있는지 확인해봅시다.
```


```python
print(1 in [3, 2])
```

    False
    


```python
# 튜플안에 특정한 정수가 있는지 확인해봅시다.
# 정수 5가 (1, 2, 'hi') 튜플에 속해있는지 확인해봅시다.
```


```python
print(5 in (1, 2, 'hi'))
```

    False
    


```python
# range안에 특정한 정수가 있는지 확인해봅시다.
# -3이 range(3) 에 속해있는지 확인해봅시다.
```


```python
# 
-3 in range(3)
```




    False




```python
# 문자열안에 특정한 문자가 있는지 확인해봅시다.
# 문자열 'a' 가 'apple' 에 속해있는지 확인해봅시다.
```


```python
print('a' in 'apple')
```

    True
    


```python
# 리스트안에 특정한 문자가 없는지 확인해봅시다.
# 문자열 'b' 가 'apple' 에 속해있는지 확인해봅시다.
```


```python
print('a' in 'apple')
```

    True
    

## 시퀀스형 연산자(Sqeuence Type Operator)

### 산술 연산자 (+)
시퀀스를 연결(concatenation)할 수 있습니다. 


```python
# 두 list [1, 2] 와 ['a'] 를 + 를 이용하여 합쳐봅시다.
```


```python
print([1, 2] + ['a'])
```

    [1, 2, 'a']
    


```python
# 두 튜플 (1, 2) 와 ('a',) 를 + 를 이용하여 합쳐봅시다.
```


```python
print((1, 2) + ('a',))
#뒤에 쉼표 조심!!!
```

    (1, 2, 'a')
    


```python
# range에는 사용할 수 없습니다.
# range(1), range(2, 5) 를 + 를 이용하여 합치고자 할 때 발생하는 오류를 확인해 봅시다.
```


```python
print(range(1) + range(2, 5))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [64], in <cell line: 1>()
    ----> 1 print(range(1) + range(2, 5))
    

    TypeError: unsupported operand type(s) for +: 'range' and 'range'



```python
# 두 문자열 '12' 와 'a' 를 + 를 이용하여 합쳐봅시다.
```


```python
print('12' + 'a')
```

    12a
    

### 반복 연산자 (*)
시퀀스를 반복할 수 있습니다.


```python
# 리스트 [0] 을 *을 이용해 8번 반복해봅시다.
```


```python
print([0] * 8)
```

    [0, 0, 0, 0, 0, 0, 0, 0]
    


```python
# 튜플 (1, 2) 를 * 을 활용해 3번 반복해봅시다.
```


```python
print((1, 2) * 3)
```

    (1, 2, 1, 2, 1, 2)
    


```python
# range에는 사용할 수 없습니다.
# range(1) 을 * 연산자로 3번 반복하려고 할 때 발생하는 오류를 확인해 봅시다.
```


```python
print(range(1) * 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [68], in <cell line: 1>()
    ----> 1 print(range(1) * 3)
    

    TypeError: unsupported operand type(s) for *: 'range' and 'int'



```python
# 문자열 'hi' 를 * 을 활용해 3번 반복해봅시다.
```


```python
'hi' * 3
```




    'hihihi'



## 기타 : 인덱싱/슬라이싱 (Indexing/Slicing)
`[]`를 통한 값을 접근하고, `[:]`을 통해 슬라이싱할 수 있습니다. (data structure 챕터에서 자세하게 학습합니다.)

### 인덱싱
시퀀스의 특정 인덱스 값에 접근 할 수 있습니다.
- 해당 인덱스가 없는 경우 IndexError가 발생합니다.


```python
# 리스트를 인덱싱을 통해 값에 접근해봅시다.
# 리스트 [1, 2, 3]의 세번째 값을 인덱싱으로 확인해봅시다.
```


```python
print([1, 2, 3].index(3))
```

    2
    


```python
# 튜플을 인덱싱을 통해 값에 접근해봅시다.
# 튜플 (1, 2, 3)의 첫번째 값을 인덱싱으로 확인해봅시다.
```


```python
print((1, 2, 3).index(1))
```

    0
    


```python
# range를 인덱싱을 통해 값에 접근해봅시다.
# range(3)의 세번째 값을 인덱싱으로 확인해봅시다.
```


```python
print(range(3).index(2))
print(range(3))
```

    2
    range(0, 3)
    


```python
# 문자열을 인덱싱을 통해 값에 접근해봅시다.
# 문자열 'abc'의 첫번째 값을 인덱싱으로 확인해봅시다.
```


```python
'abc'[0]
```




    'a'




```python
# 찾고자 하는 인덱스가 존재하지 않을때 오류가 발생합니다.
# 문자열 apple의 100번째 값을 인덱싱으로 확인하고자 할 때 발생하는 오류를 확인해봅시다.
```


```python
'apple'[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Input In [112], in <cell line: 1>()
    ----> 1 'apple'[100]
    

    IndexError: string index out of range


### 슬라이싱
- Sequence[start:end[:step]]

시퀀스를 특정 단위로 슬라이싱 할 수 있습니다.


```python
# 아래 코드들을 실행한 결과를 확인하여 슬라이싱의 작동 원리를 파악해봅시다.
print([1, 2, 3, 4][1:4])
print((1, 2, 3)[:2])
print(range(10)[5:8])
print('abcd'[2:4])
```

    [2, 3, 4]
    (1, 2)
    range(5, 8)
    cd
    

시퀀스를 `k` 간격으로 슬라이싱 할 수 있습니다.


```python
# 아래 코드들을 실행한 결과를 확인하여 슬라이싱의 작동 원리를 파악해봅시다.
# 문자열, 튜플, 레인지에서 모두 동일하게 동작합니다.
print([1, 2, 3, 4][0:4:2])
```

    [1, 3]
    


```python
# 아래의 코드를 실행하여 결과를 확인해 봅시다.
s = 'abcdefghi'
```


```python
print(s[:3])
print(s[5:])
print(s[::])
print(s[::-1])
```

    abc
    fghi
    abcdefghi
    ihgfedcba
    

## 연산자 우선순위

0. `()`을 통한 grouping

1. Slicing

2. Indexing

3. 제곱연산자
    `**`

4. 단항연산자 
    `+`, `-` (음수/양수 부호)

5. 산술연산자
    `*`, `/`, `%`
    
6. 산술연산자
    `+`, `-`
 
7. 비교연산자, `in`, `is`

8. `not`

9. `and` 

10. `or`

[파이썬 문서](https://docs.python.org/ko/3/reference/expressions.html#operator-precedence)



```python
# 우선순위를 확인해봅시다.
```


```python
# -3 ** 6의 값을 확인해봅시다.
```


```python
print(-3 ** 6)
```

    -729
    


```python
# (-3) ** 6의 값을 확인해봅시다.
```


```python
print((-3) ** 6)
```

    729
    

# 정리

## 변수(Variable)와 자료형(Data Type)

<center><img width=800 height=400 src="https://user-images.githubusercontent.com/9452521/87640197-55a7f280-c781-11ea-9cff-19c022ce704a.png", alt="variable"/></center>


## 컨테이너(Container)
<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>

# 프로그램 구성 단위

## 식별자(identifier)
- 변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질수 있는 이름을 의미합니다.
- 예약어는 사용이 불가능합니다.

## 리터럴(literal)
- 읽혀지는 대로 쓰여있는 값 그 자체를 의미합니다.


```python
# name은 식별자 == 변수
# '김싸피'은 리터럴
name = '김싸피'
```

## 표현식 (Expression)
- 새로운 데이터 값을 생성하거나 계산하는 코드 조각을 의미합니다.

## 문장 (Statement)
- 특정한 작업을 수행하는 코드 전체를 의미합니다.
- 파이썬이 실행 가능한 최소한의 코드 단위를 말합니다.
- 표현식은 값을 생성하는 일부분이고, 문장은 특정 작업을 수행하는 코드 전체 입니다.

### 문장과 표현식의 관계

<center><img width="600" height="300" src="https://user-images.githubusercontent.com/9452521/87619771-f41f5e00-c757-11ea-9e4b-1f76e4ca0981.png", alt="variable"/></center>


```python
# 하나의 값(value)도 문장이 될 수 있습니다.
'ssafy'
```


```python
# 표현식(expression)도 문장이 될 수 있습니다.
5 * 21 - 4
```


```python
# 실행 가능(executable)해야 하기 때문에 아래의 코드는 문장이 될 수 없습니다.
name = '
```

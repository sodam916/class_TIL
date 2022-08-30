<p style="font-size: 33px; font-weight: 700; margin-bottom: 3rem">에러 & 예외 처리</p>

- 에러(Error)
- 예외 처리(Exception Handling)

[파이썬 문서](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)


# 에러(Error)
발생할 수 있는 에러의 종류를 확인해봅시다.

## 문법 에러(Syntax Error)

> 문법 에러가 있는 프로그램은 실행되지 않습니다.

* 에러 발생 시 `SyntaxError`라는 키워드와 함께, 에러의 상세 내용을 보여줍니다.


* `파일이름`과 `줄번호`, `^` 문자를 통해 파이썬이 코드를 읽어 들일 때(`parser`) 문제가 발생한 위치를 표현합니다.


* `parser` 는 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(`^`)를 표시합니다.


```python
# 조건문을 통해 문법 에러를 발생시켜봅시다.

# 다음 코드는 else 문 뒤에 콜론이 누락되어 있습니다.
# 코드를 실행시켜보고 invalid syntax 오류를 확인해 봅시다.

if True:
    print('참')
else
    print('거짓')
    
    #SyntaxError: invalid syntax
```


```python
# print 문을 통해 다른 오류를 발생시켜봅시다.

# 다음 코드는 닫는 따옴표가 누락되어 있습니다.
# 코드를 실행시켜보고 EOL 오류(따옴표 오류)를 확인해 봅시다.

print('hi)
      
      #SyntaxError: EOL while scanning string literal
```


```python
# 코드를 실행시켜보고 EOF 에러(괄호 닫기 오류)를 확인해 봅시다.

print('hi'
      #SyntaxError: unexpected EOF while parsing
```


```python
# 정확한 에러 위치를 지정하지 않을 수도 있습니다.

# 다음 코드의 조건문에는 콜론이 누락되어 있습니다.
# 코드를 실행시켜보고 문법 오류를 확인해 봅시다.

if True print('참')
```

## 예외(Exception)

> 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춥니다.

* 문법적으로는 옳지만, 실행 시 발생하는 에러입니다.


* *아래 제시된 모든 에러는 `Exception`을 상속받아 이뤄집니다.*

`ZeroDivisionError`
- 파이썬에서는 어떤 수를 0으로 나누게 되면 에러가 발생합니다.


```python
# 어떤 수를 0으로 나누는 코드를 작성해 보고 오류를 확인해 봅시다.

print(5 / 0) #ZeroDivisionError: division by zero
```

`NameError`
- 지역 혹은 전역 이름 공간 내에서 유효하지 않는 이름은 사용할 수 없습니다. <br>즉, 어느 곳에서도 정의되지 않은 변수를 호출하였을 경우 에러가 발생합니다.


```python
# abc라는 변수를 print로 출력해 보고 오류를 확인해 봅시다.

print(abc) # NameError: name 'abc' is not defined
```

`TypeError`
- 자료형이 올바르지 못한 경우


```python
# 숫자 1과 문자 1을 더하는 코드를 작성해 보고 오류를 확인해 봅시다.

print( 1 + '1') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
```


```python
# round 함수는 어떤 수를 반올림해 주는 내장 함수입니다.
# round 함수에 숫자가 아닌 문자를 넣어보고 발생하는 오류를 확인해 봅시다.

print(round('4')) #TypeError: type str doesn't define __round__ method
```

- 함수 호출 과정에서 필수 매개변수가 누락된 경우


```python
# 내장 random 모듈을 불러오세요.
# random.sample() 함수는 2개의 매개변수를 받도록 정의되어 있습니다.
# random.sample() 함수에 숫자 3개가 담긴 리스트만 넣고 호출해 보세요.
# 그리고 매개변수가 누락되어 발생하는 오류를 확인해 봅시다.

import random

print(random.sample(1,2,3))
#TypeError: sample() takes 3 positional arguments but 4 were given
```

- 함수 호출 과정에서 매개변수 개수가 초과해서 들어온 경우


```python
# random.choice() 함수는 하나의 매개 변수만 받도록 정의되어 있습니다.
# 숫자 3개가 담긴 리스트와, 숫자 6을 넣고 호출해 보세요.
# 그리고 매개변수가 초가 되어 발생하는 오류를 확인해 봅시다.

a = [1, 2, 3]
print(random.choice(a,6))
#TypeError: choice() takes 2 positional arguments but 3 were given
```

`ValueError`
- 자료형은 올바르나 값이 적절하지 않은 경우


```python
# int()는 정수가 아닌 값을 받았을 경우 에러가 발생합니다.
# int() 안에 문자 3.5를 넣고 호출한 뒤 발생하는 오류를 확인해 봅시다.

print(int('3.5'))
#ValueError: invalid literal for int() with base 10: '3.5'
```

- 존재하지 않는 값을 찾고자 할 경우


```python
# index()는 리스트에서 찾고자 하는 값의 인덱스를 반환합니다.
# numbers 리스트에 없는 값인 3을 찾게 되면 에러가 발생합니다.
# 코드를 실행시킨 뒤 발생하는 오류를 확인해 봅시다.

numbers = [1, 2]
numbers.index(3)
#ValueError: 3 is not in list
```

`IndexError`
- 존재하지 않는 index로 조회할 경우


```python
# 비어있는 리스트는 어떤 인덱스 값으로든 접근할 수 없습니다.
# 코드를 실행시켜서 비어있는 empty_list를 -1 인덱스로 접근했을 때 발생하는 오류를 확인해 봅시다.

empty_list = []
empty_list[-1]
#IndexError: list index out of range
```

`KeyError`
- 존재하지 않는 Key로 접근한 경우


```python
# 아래 songs라는 딕셔너리에는 'sia'라는 Key만 존재하며,
# 'queen'이라는 키는 존재하지 않습니다.
# 코드를 실행시켜보고 발생하는 오류를 확인해 봅시다.

songs = {'sia': 'candy cane lane'}
songs['queen']
#KeyError
```

`ModuleNotFoundError`
- 존재하지 않는 Module을 `import` 하는 경우


```python
# 파이썬에 존재하지 않는 모듈인 "reque"라는 이름의 모듈을 불러와봅시다(import).
# 그리고 발생하는 오류를 확인해 봅시다.
import reque
# ModuleNotFoundError
```

`ImportError`
- Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우


```python
# 파이썬 내장 random 모듈은 존재하나 그 안에 "sampl"이라는 함수는 존재하지 않습니다.
# random 모듈을 불러와서 "sampl"이라는 함수를 불러와보고, 발생하는 오류를 확인해 봅시다.

random.sampl
# AttributeError: module 'random' has no attribute 'sampl'
```

`KeyboardInterrupt`
- 사용자가 임의로 실행을 중단한 경우
- 주피터 노트북에서는 정지 버튼이지만, 실제로 우리가 돌릴 때는 `ctrl`+`c`를 통해 종료하였을 때 발생합니다.


```python
# 무한 반복되는 while 문을 실행시켜보고, 정지시켜보세요.
# 그리고 발생하는 오류를 확인해 봅시다.

while 1:
    b = []
    a = '1'
    b += a
return b
#KeyboardInterrupt: 

```

`IndentationError`
- Indentation(들여 쓰기)이 적절하지 않은 경우


```python
# 코드를 실행해서 발생하는 오류를 확인해 봅시다.

for i in range(3):
print(i)
# IndentationError: expected an indented block
```


```python
# 코드를 실행해서 발생하는 오류를 확인해 봅시다.

for i in range(3):
    print(i)
        print(i)
        
# IndentationError: unexpected indent
```

# 예외 처리(Exception Handling)

## `try` & `except`
`try`문과 `except`절을 사용하여 예외 처리를 할 수 있습니다.


### 기초 문법

```python
try:
    <코드 블록 1>
except (예외):
    <코드 블록 2>
```

* `try` 아래의 코드 블록(code block)이 실행됩니다.

* 예외가 발생되지 않으면, **`except` 없이 실행이 종료됩니다.**

* 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행됩니다.


```python
# 사용자로부터 값을 받아 정수로 변환하여 출력해 봅시다.
# input() 함수를 이용하여 사용자로부터 입력을 받은 뒤
# 해당 값을 정수로 변환하여 출력해 보세요.
a = input()
print(int(a))

```


```python
# 위에서 배운 try-except 구문을 활용해 봅시다.
# 사용자가 문자열을 넣어 해당 오류(ValueError)가 발생하면
# 숫자를 입력하라고 출력해 봅시다.

try :
    a = input()
    print(int(a))    
except:
    print('숫자를 입력해주세요')
```

### 복수의 예외 처리

하나 이상의 예외를 모두 처리할 수 있습니다.

괄호가 있는 튜플로 여러 개의 예외를 지정할 수 있습니다.

---

**활용법**

```python
try:
    <코드 블록 1>
except (예외 1, 예외 2):
    <코드 블록 2>

try:
    <코드 블록 1>
except 예외 1:
    <코드 블록 2>
except 예외 2:
    <코드 블록 3>
```


```python
# 숫자 100을 사용자가 입력한 값으로 나눈 후 출력하는 코드를 작성해 봅시다.

# input() 함수를 이용하여 사용자로부터 입력을 받으세요.
# 해당 값을 정수로 변환한 뒤, 숫자 100을 입력받은 값으로 나누는 코드를 작성해 보세요.

a = input()
print(100/int(a))
```


```python
# 문자열일 때와 0일 때의 경우를 모두 처리를 해봅시다.

# 어떤 값을 숫자가 아닌 값으로 나눌 때 발생하는 에러는 ValueError입니다.
# 어떤 값을 0으로 나눌 때 발생하는 에러는 ZeroDivisionError입니다.
# try-except 구문을 활용하여 위의 두 오류를 처리해 보세요.

try :
    a = input()
    print(100/int(a))
except (ValueError, ZeroDivisionError):
    print('숫자를 입력해야합니다')
    
```


```python
# 각각 다른 오류를 출력할 수 있습니다.
# 여러 개의 except 구문을 활용해 보세요.
# (ValueError, ZeroDivisionError)

try :
    a = input()
    print(100/int(a))
except ValueError:
    print('숫자를 입력하세요')
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다')
except:
    print('에러가 발생하였습니다')

```

    가나다
    숫자를 입력하세요
    

- 중요! <br>**에러가 순차적으로 수행됨**으로, 가장 작은 범주부터 시작해야 합니다.


```python
# Exception은 가장 큰 범주의 에러로써 모든 에러를 처리할 수 있습니다.
# 따라서 아래 코드는 숫자가 아닌 값을 넣었을 때 순차적으로 먼저 적힌 Exception 에러가 발생합니다.
# 코드를 실행하고 결과를 확인해 봅시다.

try:
    num = input('값을 입력하시오: ')
    100/int(num)
except Exception: # Exception 은 가장 큰 범주
    print('모르겠지만 에러야')
except ValueError:
    print('숫자를 넣어')
```

    값을 입력하시오: 가나다
    모르겠지만 에러야
    

### `else`

* 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용합니다.
* 모든 `except` 절 뒤에 와야 합니다.
* `try` 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 적절합니다.
---

**활용법**

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```


```python
# else를 사용해봅시다.
try :
    numbers = [1, 2, 3]
    number = numbers[3]
    
except :
    print('오류 발생')
    
else:
    print(number * 100)

# try 구문에서 numbers라는 이름의 리스트에 숫자 3개를 저장하세요.
# 그리고 존재하지 않는 인덱스의 값을 가져와서 number 변수에 저장하세요.
# (이 때, 존재하지 않는 인덱스를 참고하는 경우 IndexError가 발생하게 됩니다.)
# except 구문에서 IndexError가 발생할 경우 '오류 발생'이라는 메세지를 출력하세요.
# 마지막으로 else 구문을 활용하여 number * 100을 출력해보세요.


```

    오류 발생
    

### `finally` 

* 반드시 수행해야 하는 문장은 `finally`를 활용합니다.
* 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용합니다.
* 예외의 발생 여부와 관계없이 `try` 문을 떠날 때 항상 실행합니다.

---

**활용법**

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```


```python
# finally를 사용해봅시다.
# 다음 코드에서 finally 구문을 활용하여 '성적 파일을 종료합니다'라는 메세지를 출력해보세요.

try:
    print('성적 파일을 읽어옵니다.')
    data = {'python': 'A+'}
    data['java']
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
finally:
    print('성적 파일을 종료합니다')


```

    성적 파일을 읽어옵니다.
    'java'는 딕셔너리에 없는 키입니다.
    성적 파일을 종료합니다
    

### 에러 메시지 처리  `as`

`as` 키워드를 활용하여 에러 메시지를 보여줄 수도 있습니다.

---

**활용법**

```python
try:
    <코드 블럭 1>
except 예외 as err:
    <코드 블럭 2>
```


```python
# except 구문에서 발생하는 에러 메세지를 코드 블럭에 넘겨줄 수도 있습니다.

# 다음 코드에서 as를 활용하여 에러 메세지를 그 아래 코드 블럭에 넘겨보세요.
# 그리고 as로 명명한 에러 메세지를 print를 이용하여 출력해보세요.

try:
    empty_list = []
    print(empty_list[-1])
except IndexError as err:
    print(f'{err}, 오류가 발생했습니다.')
    
#list index out of range, 오류가 발생했습니다.    

    

```

    list index out of range, 오류가 발생했습니다.
    

## 예외 발생 시키기(Exception Raising)



### `raise`
`raise`를 통해 예외를 강제로 발생시킬 수 있습니다.

---

**활용법**

```python
raise <에러>('메시지')
```


```python
# raise를 사용해 봅시다.

# raise만 작성한 뒤 실행시켜봅시다.
# 코드를 실행시켜보고 결과를 확인하세요.

raise
# RuntimeError: No active exception to reraise
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    Input In [12], in <cell line: 6>()
          1 # raise를 사용해 봅시다.
          2 
          3 # raise만 작성한 뒤 실행시켜봅시다.
          4 # 코드를 실행시켜보고 결과를 확인하세요.
    ----> 6 raise
    

    RuntimeError: No active exception to reraise



```python
# 이번에는 ValueError() 오류를 raise 해봅시다.
# 코드를 실행시켜보고 결과를 확인하세요.

raise ValueError('hi')
#ValueError: hi
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [13], in <cell line: 4>()
          1 # 이번에는 ValueError() 오류를 raise 해봅시다.
          2 # 코드를 실행시켜보고 결과를 확인하세요.
    ----> 4 raise ValueError('hi')
    

    ValueError: hi


### [연습] `raise` 예외 발생시키기

> 리스트를 받아 평균을 반환하는 함수 `avg`를 작성하세요.

---

- `scores`의 길이가 0인 경우 `Exception`과 메시지를 발생시키세요.
    - *예) Exception: 학생이 없습니다.*

- 정상적인 경우에는 평균을 `return`합니다.


```python
def avg(scores):
    if len(scores) == 0:
        raise Exception('학생이 없습니다')
    return (sum(scores) / len(scores))




```


```python
# 다음 코드를 통해 올바른 결과가 나오는지 확인하세요.
avg([])
```


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    Input In [28], in <cell line: 2>()
          1 # 다음 코드를 통해 올바른 결과가 나오는지 확인하세요.
    ----> 2 avg([])
    

    Input In [27], in avg(scores)
          1 def avg(scores):
          2     if len(scores) == 0:
    ----> 3         raise Exception('학생이 없습니다')
          4     return (sum(scores) / len(scores))
    

    Exception: 학생이 없습니다


### `assert`

`assert` 문은 예외를 발생시키는 다른 방법입니다. 

보통 **상태를 검증하는데 사용**되며 무조건 `AssertionError`가 발생합니다.

---

**활용법**

```python
assert Boolean expression, error message

assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
```

---

위의 검증식이 거짓일 경우를 발생합니다.

일반적으로 디버깅용도로 사용됩니다. [파이썬 문서](https://docs.python.org/ko/3/reference/simple_stmts.html#the-assert-statement)

```bash
$ python code.py
Traceback (most recent call last):
  File "code.py", line 1, in <module>
    assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
AssertionError: 길이가 1이 아닙니다.

$ python -O code.py

```

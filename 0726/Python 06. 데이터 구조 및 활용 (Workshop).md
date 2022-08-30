# Python 06. 데이터 구조 및 활용 (Workshop)



### 1. 무엇이 중복일까

    문자열을 전달 받아 해당 문자열에서 중복해 나타난 문자들을 담은 list를 반환하는 

    duplicated_letters 함수 작성



```python
'''
중복 문자들을 반환하는 함수
'''
def duplicated_letters(x):
    first = []
    double = []
    for let in x: 
        if let not in first:
            first.append(let)
        else:
            if let not in double:
                double.append(let)
        
    return double

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
```



### 2. 소대소대

    문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 

    반환하는 low_and_up 함수를 작성.

    이때, 전달 받는 문자열은 알파벳으로만 구성



```python
'''
소문자 대문자 번갈아 나타나는 함수
'''
def low_and_up(x):
    words = ''
    # 홀수는 소문자 짝수는 대문자
    for ind in range(len(x)): 
        if ind % 2 == 0:
            words +=  x[ind].lower()
        else:
            words += x[ind].upper()
            
    return words
            
print(low_and_up('apple'))
print(low_and_up('banana'))
```



### 3. 솔로 천국 만들기

    정수 0 ~9 로 이루어진 list를 전달 받아, 연속되는 숫자는 하나만 남기고 제거한 list를 

    반환하는 lonely 함수를 작성하시오.

    (이때, 제거된 후 남은 수의 요소는 기존의 순서를 유지한다)



```python
'''
중복수 제거 함수 
'''
def lonely(x):
    lst = [x[0]] # 리스트의 첫번째의 값 지정
    for n in range(1,len(x)): #n이 0 1 2 3 4 
        if x[n-1] != x[n]: #뒤에 수와 앞의 수가 같은지 비
            lst.append(x[n])

    return lst
        
print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
```





















    

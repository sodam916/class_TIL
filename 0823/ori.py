# 우선순위 만들기
def priority(x):
    if x == '*' or x == '/':
        return 3
    elif x == '+' or x == '-':
        return 2
    else:
        return 1


# 중위 표현식을 후위 표현식으로 바꾸기


# 계산 함수
def calculate(arr):
    stack = []
    for i in range(N):
        if arr[i] == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A + B)
        elif arr[i] == '-':
            B = stack.pop()
            A = stack.pop()
            stack.append(A - B)
        elif arr[i] == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A * B)
        elif arr[i] == '/':
            B = stack.pop()
            A = stack.pop()
            stack.append(A / B)
        else:
            stack.append(arr[i])
    return stack


# T = int(input())
for tc in range(1, 11):
    N = int(input())
    arr = input()
    stack = []
    lst = []  # 반환 리스트 만듦
    for t in range(N):
        num = priority(arr[t])  # 우선 순위 확인
        if num == 3:
            while stack:
                if priority(stack[-1]) < num:
                    break
                lst.append(stack.pop())
            stack.append(arr[t])
        elif num == 2:
            while stack:
                if priority(stack[-1]) < num:
                    break
                lst.append(stack.pop())
            stack.append(arr[t])
        else:
            lst.append(arr[t])

    while stack:
        lst.append(stack.pop())

    print(f'#{tc}', *calculate(lst))
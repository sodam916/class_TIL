
def calculate(arr):
    stack = []
    for i in range(len(arr)):
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

T = int(input())
for tc in range(1,T+1):
    prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    arr = list(input().split())

    stack = []
    lst = []

    for n in range(len(arr)):
        if arr[n].isdigit():
            lst.append(int(arr[n]))
        elif arr[n] == '(':
            stack.append((arr[n]))
        elif arr[n] == ')':
            while stack[-1] != '(':        # 여는 괄호가 나올 때 까지
                lst.append(stack.pop())
            stack.pop()
        else:
            while stack and prior[arr[n]] <= prior[stack[-1]]:
                lst.append(stack.pop())
            stack.append(arr[n])

    while len(stack) != 0:
        lst.append(stack.pop())

    print(f'#{tc}', *calculate(lst))

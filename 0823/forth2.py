
T = int(input())

for tc in range(1,T+1):
    arr = list(input().split())
    stack = []

    for i in range(len(arr)):
        if arr[i].isdigit():
            stack.append(arr[i])
        elif arr[i] == '+':
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()
                stack.append(int(A) + int(B))
            else:
                print(f'#{tc}','error')
                break
        elif arr[i] == '-':
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()
                stack.append(int(A) - int(B))
            else:
                print(f'#{tc}','error')
                break
        elif arr[i] == '*':
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()
                stack.append(int(A) * int(B))
            else:
                print(f'#{tc}','error')
                break
        elif arr[i] == '/':
            if len(stack) >= 2:
                B = stack.pop()
                A = stack.pop()
                stack.append(int(A) // int(B))
            else:
                print(f'#{tc}','error')
                break
        elif arr[i] == '.':
            if len(stack) > 2:
                print(f'#{tc}','error')
                break
            else:
                print(f'#{tc}',*stack)




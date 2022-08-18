T = int(input())
for tc in range(1, T+1):
    arr = input()
    lst = list(arr)

    size = len(lst)
    stack = []
    top = -1
    ans = []

    for i in lst:
        if i in ['(', '{', '[']:
            stack.append(i)

        elif i in [')','}',']']:
            if not stack:
                stack.append(i)
                break
            elif (i == ')' and stack[top] != '(') or (i == '}' and stack[top] != '{'):
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print(f'#{tc}','1')
    else:
        print(f'#{tc}','0')

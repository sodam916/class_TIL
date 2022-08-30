T = int(input())

def pop():
    global top
    if top != -1:
        top -= 1
        return stack[top]

for tc in range(1,T+1):
    arr = input()
    lst = list(arr)

    size = len(lst)
    stack = []
    top = -1

    for j in range(size):
        if not stack:
            stack.append(lst[j])

        else:
            if stack[-1] == lst[j]:
                stack.pop()

            else:
                stack.append(lst[j])



    ans = len(stack)
    print(ans)

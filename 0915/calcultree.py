

for tc in range(1,11):
    N = int(input())

    tree = [0] * (N+1)    #  [0, 0, 0, 10, 88, 65]
    lst = []
    cal = []
    for _ in range(N):
        arr = list(input().split())

        if len(arr) <= 2:
            tree[int(arr[0])] = int(arr[1])
        else:
            cal.append(arr)

    for _ in range(len(cal)):
        n, caln, a, b = cal.pop()
        na = tree[int(a)]
        nb = tree[int(b)]

        if caln == '+':
            tree[int(n)] = int(na) + int(nb)
        elif caln == '-':
            tree[int(n)] = int(na) - int(nb)
        elif caln == '*':
            tree[int(n)] = int(na) * int(nb)
        elif caln == '/':
            tree[int(n)] = int(na) // int(nb)

    print(f'#{tc}',tree[1])

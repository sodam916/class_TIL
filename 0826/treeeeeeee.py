
for tc in range(1, 11):
    V = int(input())
    arr = [list(map(str, input().split())) for _ in range(V)]
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    ch = [0] * (V + 1)
    ans = []

    for i in arr:
        num = int(i[0])
        ch[num] = i[1]
        if len(i) == 4:
            L[num] = int(i[2])
            R[num] = int(i[3])
        elif len(i) == 3:
            L[num] = int(i[2])

    def inorder(v):
        if v == 0:
            return
        inorder(L[v])
        print(ch[v], end='')
        inorder(R[v])
        # 방문 후위 순회

    print(f'#{tc}', end=' ')
    inorder(1)
    print()
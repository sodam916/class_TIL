import sys
sys.stdin = open("sample_input.txt")

for tc in range(1,4):
    N = int(input())

    arr = [list(map(str, input().strip())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ar = ac = 0
    a = []
    b = []
    cc = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'A':
                a.append((r,c))

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'B':
                b.append((r,c))

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'C':
                cc.append((r,c))



    for i in range(len(a)):
        x, y = a[i]
        for d in range(4):
            nr = x + dr[d]
            nc = y + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'H':
                    arr[nr][nc] = 'X'

    for i in range(len(b)):
        x, y = b[i]
        for d in range(4):
            for p in range(1,3):
                nr = x + dr[d] * p
                nc = y + dc[d] * p
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 'H':
                        arr[nr][nc] = 'X'

    for i in range(len(cc)):
        x, y = cc[i]
        for d in range(4):
            for p in range(1,4):
                nr = x + dr[d] * p
                nc = y + dc[d] * p
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 'H':
                        arr[nr][nc] = 'X'


    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'H':
                cnt += 1

    print(cnt)
    print(arr)


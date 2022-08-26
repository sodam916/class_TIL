import sys
sys.stdin = open("magnetic_input (3).txt")

for tc in range(1,2):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1]
    s = []
    n = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                s.append((r,c))
            elif arr[r][c] == 2:
                n.append((r,c))

    for i in range(len(s)):
        x, y = s[i]
        for d in range(2):
            sr = x + dr[d]
            sc = y
            if 0 <= sr < N and 0 <= sc < N:
                if arr[sr][sc] == 0:
                    sr -= 1
                    if sr == N-1:
                        sr = 0
                elif sr == N-1:
                    sr = 0
    print(arr)
    print()




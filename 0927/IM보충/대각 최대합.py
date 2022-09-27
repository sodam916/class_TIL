T = int(input())
def check(r, c):
    summ = arr[r][c]
    for d in range(4):
        for g in range(1,N):
            nr = r + dr[d] * g
            nc = c + dc[d] * g
            if 0 <= nr < N and 0 <= nc < N:
                summ += arr[nr][nc]
    return summ

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 1, -1 ]    # 우상 우하 좌하 좌상
    dc = [1, 1, -1, -1 ]
    result = []

    for r in range(N):
        for c in range(N):
            result.append(check(r,c))
    print(f'#{tc}',max(result))



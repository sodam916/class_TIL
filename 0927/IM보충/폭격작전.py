T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    summ = 0
    for _ in range(M):
        r, c, p = map(int, input().split())
        for d in range(4):
            for g in range(p+1):
                nr = r + dr[d] * g
                nc = c + dc[d] * g
                if 0 <= nr < N and 0 <= nc < N:
                    visited[nr][nc] = 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                summ += arr[i][j]

    print(f'#{tc}',summ)



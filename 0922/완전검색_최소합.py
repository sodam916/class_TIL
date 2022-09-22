T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    summ = arr[0][0]
    maxx = 9999
    dr = [1, 0]
    dc = [0, 1]
    visited = [[0] * N for _ in range(N)]
    r = c = 0

    def dfs(r, c):
        global maxx, summ
        if maxx < summ:
            return
        if r == N-1 and c == N-1:
            maxx = summ
            return

        for d in range(2):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                summ += arr[nr][nc]
                dfs(nr, nc)
                visited[nr][nc] = 0
                summ -= arr[nr][nc]

    dfs(0, 0)
    print(f'#{tc}',maxx)



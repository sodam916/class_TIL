T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sqare = [[0] * N for _ in range(N)]
    visited = [[0] * (N+2) for _ in range(N+2)]
    for check in range(0,N+1):
        visited[check][0] = 1
        visited[check][N+1] = 1
        visited[0][check] = 1
        visited[N+1][check] = 1

    dr = [0, 1, 0, -1]    # 우 하 좌 상
    dc = [1, 0, -1, 0]
    r = c = 1
    a = 0
    e = N
    s = 0
    idx = [(r,c)]
    visited[r][c] = 1
    while True:
        if len(idx) == (N*N):
            break
        elif a == 4:
            a = 0
        else:
            nr = r + dr[a]
            nc = c + dc[a]
            if visited[nr][nc] == 1:
                a += 1
            else:
                r = nr
                c = nc
                idx.append((nr,nc))
                visited[nr][nc] = 1
    j = 1
    for i in idx:
        x, y = i
        sqare[x-1][y-1] = j
        j += 1

    print(f'#{tc}')
    for j in sqare:
        print(*j)
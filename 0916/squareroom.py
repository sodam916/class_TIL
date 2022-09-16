T = int(input())


def dfs(r, c):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if room[nr][nc] == (room[r][c] + 1):
                path.append(room[nr][nc])
                dfs(nr, nc)

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start = []
    maxx = []
    ans = []
    ans2 = []

    for i in range(N):
        for j in range(N):
            start.append((i,j))

    while start:
        path = []
        r, c = start.pop()
        dfs(r, c)
        ans.append(path)
        maxx.append(len(path))
    m = max(maxx)

    for n in range(N**2):
        if len(ans[n]) == m:
            ans2.append(ans[n][0]-1)

    print(f'#{tc}',min(ans2), m+1)




    # while start:
    #     path = []
    #     x, y = start.pop()
    #     path.append(room[x][y])
    #     for d in range(4):
    #         nr = x + dr[d]
    #         nc = y + dc[d]
    #         if 0 <= nr < N and 0 <= nc < N:
    #             if room[nr][nc] == (room[x][y] + 1):
    #                 cnt += 1
    #                 path.append(room[nr][nc])
    #                 x, y = nr, nc
    #             else:
    #                 cnt = 0
    #     print(path)
    #     print(cnt)









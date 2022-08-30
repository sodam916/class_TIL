T = int(input())

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    stack = []

    sr = sc = er = ec = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
            elif maze[i][j] == 3:
                er, ec = i, j
    stack = [(sr, sc)]
    visited[sr][sc] = 0

    while stack:
        for n in range(4):
            nr, nc = (sr + dx[n]), (sc + dy[n])

            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 경계 체크
                continue

            if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                stack.append((sr, sc))
                visited[nr][nc] = 1
                sr, sc = nr, nc
                break
        else:
            sr, sc = stack.pop()

    print(visited)
    print(visited[er][ec])










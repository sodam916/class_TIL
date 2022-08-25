import sys
sys.stdin = open("maze_input (2).txt")


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]

    visited = [[0] * 16 for _ in range(16)]

    sr = sc = er = ec = 0
    for r in range(16):
        for c in range(16):
            if arr[r][c] == 2:
                sr = r
                sc = c
            if arr[r][c] == 3:
                er = r
                ec = c

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = [(sr,sc)]
    visited[sr][sc] = 1

    while Q:
        x, y = Q.pop()
        if x == er and y == ec:
            print(f'#{tc}','1')
            break

        for d in range(4):
            nr = x + dr[d]
            nc = y + dc[d]
            if 0 <= nr < 16 or 0 <= nc < 16:
                if visited[nr][nc] == 0 and arr[nr][nc] != 1:
                    visited[nr][nc] = 1
                    Q.append((nr,nc))

    else:
        print(f'#{tc}','0')




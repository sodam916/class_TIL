N = int(input())

maze = [list(map(int, input().split())) for _ in range((N))]

visited = [[0] * N for _ in range(N)]

s = []

r = c = er = ec = 0
for i in range(N):
    for j in range(N):
        if maze[i][j] == 2:
            r , c = i, j
        elif maze[i][j] == 3:
            er, ec = i, j

# 시작점 방문 스택에 push
S = [(r, c)]
visited[r][c] = 0

# 빈 스택이 아닐동안 반복
while S:


N = 10
arr = [[0] *N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

r = c = '*'

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    arr[nr][nc] = i + 1




for line in arr:
    print(*line)


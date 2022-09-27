T = int(input())

def dfs(k, s):
    global line
    global minn
    if minn < s:
        return
    if k == N:
        if minn > s:
            minn = s
            return
    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1
            s += line[k][i]
            dfs(k+1, s)
            visited[i] = 0
            s -= line[k][i]


for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    minn = 999999
    dfs(0, 0)
    print(f'#{tc}',minn)



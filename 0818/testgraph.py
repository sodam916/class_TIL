import sys
sys.stdin = open("graphway_input.txt")

T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]   # 인접 행렬
    visited = [0] * (V + 1)

    # 간선수만큼 입력 처리
    for _ in range(E):
        u, v = map(int, input().split())

        G[u].append(v)

    s, g = map(int, input().split())

    def dfs(v): # v = 방문할 정점 번호
        visited[v] = 1 # v를 방문한다.
        # v의 인접 정점을 w를 찾는다.
        for w in G[v]:
            if not visited[w]:
                dfs(w)
    dfs(s)
    print(f'#{tc}',visited[g])




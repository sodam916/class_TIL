T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    for i in range(0, E*2, 2):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    s, g = map(int, input().split())

    def BFS(s):
        visit = [0] * (V + 1)
        Q = [s]
        visit[s] = 1
        while Q:
            v = Q.pop(0)
            for w in G[v]:
                if not visit[w]:
                    Q.append(w)
                    visit[w] = visit[v] + 1
        print(f'#{tc}',visit[g] - 1)
    BFS(s)


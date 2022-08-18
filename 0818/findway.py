import sys
sys.stdin = open("findway_input.txt")


for tc in range(1, 11):
    T, E = map(int, input().split())
    G = [[] for _ in range(100)]    # 인접 행렬
    visited = [0] * (100)    # 방문 일단 0으로 체크

    arr = list(map(int, input().split()))
    lst = []
    for num in range(0,len(arr),2):
        lst.append(arr[num:num+2])
    for i in lst:
        u = i[0]
        v = i[1]

        G[u].append(v)


    def dfs(y):  # v = 방문할 정점 번호
        visited[y] = 1  # v를 방문한다.
        # v의 인접 정점을 w를 찾는다.
        for w in G[y]:
            if not visited[w]:
                dfs(w)
    dfs(0)
    print(f'#{tc}',visited[99])
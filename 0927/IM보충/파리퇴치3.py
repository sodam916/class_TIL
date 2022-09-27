T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = []
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    ddr = [-1, 1, 1, -1 ]    # 우상 우하 좌하 좌상
    ddc = [1, 1, -1, -1 ]

    for r in range(N):
        for c in range(N):
            summ = table[r][c]
            for d in range(4):
                for g in range(1,M):
                    nr = r + dr[d] * g
                    nc = c + dc[d] * g
                    if 0 <= nr < N and 0 <= nc < N:
                        summ += table[nr][nc]
                        result.append(summ)
            summ = table[r][c]
            for d in range(4):
                for g in range(1, M):
                    nr = r + ddr[d] * g
                    nc = c + ddc[d] * g
                    if 0 <= nr < N and 0 <= nc < N:
                        summ += table[nr][nc]
                        result.append(summ)
    print(f'#{tc}',max(result))



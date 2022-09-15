T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [[0] * N for _ in range(N)]
    # 첫 바둑알 세팅
    table[N//2-1][N//2-1] = 2
    table[N//2][N//2] = 2
    table[N//2-1][N//2] = 1
    table[N//2][N//2-1] = 1

    #방향 설정
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ddr = [1, 1]
    ddc = [-1, 1]

    for _ in range(M):
        bc, br, ball = map(int, input().split())
        table[br-1][bc-1] = ball
        if ball == 1:
            while True:
                for i in range(4):
                    nr = br + dr[i]
                    nc = bc + dc[i]
                    if nr < 0 or nr >= N or nc >= N or nc < 0:
                        continue
                    if table[nr][nc] == 2:
                        table[nr][nc] = 1
                        br, bc = nr, nc
                        break
                if i == 4:
                    break
    print(table)




T = int(input())


def checkball(br, bc, ball):
    path = []
    for d in range(8):
        for g in range(1, N):
            nr = br + dr[d] * g
            nc = bc + dc[d] * g
            if 0 <= nr < N and 0 <= nc < N:
                path.append((nr,nc))
                if table[nr][nc] == ball:

                else:
                    path = []
                    break
    print(path)
    if ball == 1 and len(path) != 0:
        for j in path:
            x, y = j
            if table[x][y] == 2:
                table[x][y] = 1

    elif ball == 2 and len(path) != 0:
        for j in path:
            x, y = j
            if table[x][y] == 1:
                table[x][y] = 2





for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [[0] * N for _ in range(N)]
    # 첫 바둑알 세팅
    table[N//2-1][N//2-1] = 2
    table[N//2][N//2] = 2
    table[N//2-1][N//2] = 1
    table[N//2][N//2-1] = 1

    #방향 설정
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]
    path = []
    black = 0
    white = 0
    for _ in range(M):
        bc, br, ball = map(int, input().split())
        table[br-1][bc-1] = ball
        checkball(br-1, bc-1, ball)
        # if ball == 1 and len(path) != 0:
        #     for j in path:
        #         x, y = j
        #         if table[x][y] == 2:
        #             table[x][y] = 1
        #
        # elif ball == 2 and len(path) != 0:
        #     for j in path:
        #         x, y = j
        #         if table[x][y] == 1:
        #             table[x][y] = 2



    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                black += 1
            elif table[i][j] == 2:
                white += 1
    print(f'#{tc}',black, white)
    print(table)








T = int(input())

def time(r,c,mic, d):
    for i in range(1, len(tablelist)):
        if timetable[i-1] == timetable[i]:
            x, y = timetable[i-1]
            othertable[x][y] =






for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    table = [[0] * N for _ in range(N)]
    othertable = [[0] * N for _ in range(N)]
    timetable = {}
    tablelist = []
    for _ in range(K):
        r, c, mic, d = map(int, input().split())
        table[r][c] = mic
        nr = r + dr[d - 1]
        nc = c + dc[d - 1]
        if (nr, nc) not in tablelist:
            tablelist.append((nr,nc))
        else:
            timetable[(r,c)] = (nr,nc)
            tablelist.append((nr,nc))

    print(tablelist)
    print(timetable)




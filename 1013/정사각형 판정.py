T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(str, input().strip())) for _ in range(N)]
    pointr = []
    pointc = []

    for r in range(N):
        for c in range(N):
            if board[r][c] == '#':
                pointr.append(r)
                pointc.append(c)

    x = pointr[-1] - pointr[0]
    y = pointc[-1] - pointc[0]

    ans = 'yes'

    if x != y:
        ans = 'no'

    elif x == y:
        for r in range(pointr[0], pointr[-1]+1):
            for c in range(pointc[0], pointc[-1]+1):
                if board[r][c] == '.':
                    ans = 'no'


    print(f'#{tc}', ans)
T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    map = [list(map(str, input().strip())) for _ in range(H)]
    N = int(input())
    play = str(input())
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    rule = {
        'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)
    }

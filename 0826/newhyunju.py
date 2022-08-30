for tc in range(1, 11):
    T = int(input())
    N, Q = map(int,input().split())
    case = [list(map(int, input().split())) for _ in range(Q)]
    ans = []

    for i in range(Q):
        L = case[i][0]
        R = case[i][1]

        
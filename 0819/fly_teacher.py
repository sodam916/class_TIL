import sys
sys.stdin = open("fly_input.txt")

T = int(input())

for tc in range(1,T+1):

    def rect_traverse(r,c, M):
        summ = 0
        for i in range(r, r+M):
            for j in range(c, c+M):
                summ += arr[i][j]


    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    summ = 0

    for r in range(N - M + 1):
        for c in range(N - M +1):

            # 좌상단 (r, c), 너비/높이 M
            ret = rect_traverse(r, c, M)
            if summ < ret:
                summ = ret

    print(summ)
    # for line in arr:
    #     print(*line)

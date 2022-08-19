import sys
sys.stdin = open("fly_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = []
    maxv = 0
    # 찾을 배열

    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            result = 0
            for r in range(M):
                for c in range(M):
                    result += (arr[i+r][j+c])

                if maxv < result:
                    maxv = result
    print(f'#{tc}',maxv)




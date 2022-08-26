T = int(input())

for tc in range(1, T+1):

    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for r in range(0,N-M+1):
        for c in range(0,N-M+1):
            summ = 0
            for n in range(M):
                for m in range(M):
                    summ += arr[r+n][c+m]
            ans.append(summ)

    print(f'#{tc}',max(ans))
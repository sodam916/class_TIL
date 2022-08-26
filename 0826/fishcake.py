T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = []
    yaki = ((arr[-1] // M) * K) - len(arr)

    if arr[0] < M:
        ans.append('Impossible')

    if K == 1:
        for n in range(N):
            if arr[n] % M != 0 and yaki <= 0:
                ans.append('Impossible')

    else:
        if yaki <= 0:
            ans.append('Impossible')

    if len(ans) == 0:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')













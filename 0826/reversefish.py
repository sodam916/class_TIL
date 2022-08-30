T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = []
    yaki = ((arr[-1] // K) * M) - len(arr)

    if arr[0] > M:
        ans.append('Possible')

    if K == 1:
        for n in range(N):
            if arr[n] % M == 0:
                ans.append('Possible')

    else:
        if yaki >= 0:
            ans.append('Possible')

    if len(ans) == 2:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
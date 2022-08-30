T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    Q = [0] * (N+1)

    r = -1
    f = -1

    for n in range(N):
        r += 1
        Q[r] = arr[n]

    for m in range(M):
        r = (r + 1) % (N+1)
        f = (f + 1) % (N + 1)
        Q[r] = Q[f]





    print(f'#{tc}',Q[(f + 1) % (N + 1)])
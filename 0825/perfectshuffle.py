T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))
    result = []
    farr = []
    barr = []
    m = N // 2
    if N % 2 == 0:
        for f in range(m):
            farr.append(card[f])
        for b in range(m,N):
            barr.append(card[b])
    else:
        for f in range(m+1):
            farr.append(card[f])
        for b in range(m+1, N):
            barr.append(card[b])
    a1 = 0
    a2 = 0
    for i in range(1,N+1):
        if i % 2 != 0:
            result.append(farr[a1])
            a1 += 1
        else:
            result.append(barr[a2])
            a2 += 1

    print(f'#{tc}',*result)



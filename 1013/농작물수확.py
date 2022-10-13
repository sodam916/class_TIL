T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input().strip())) for _ in range(N)]
    mid = N // 2 # 2
    food = 0
    a = -1
    for r in range(0,mid+1):
        a += 1
        for c in range(mid-a,mid+a+1):
            food += farm[r][c]

    for r in range(mid+1,N):
        a -= 1
        for c in range(mid-a,mid+a+1):
            food += farm[r][c]

    print(f'#{tc}',food)


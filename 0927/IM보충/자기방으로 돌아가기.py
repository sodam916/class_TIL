T = int(input())

for tc in range(1, T+1):
    N = int(input())
    road = [0] * 401
    for _ in range(N):
        n, g = map(int, input().split())
        n = (n+1) // 2
        g = (g+1) // 2

        for i in range(n, g+1):
            road[i] += 1

    print(f'#{tc}',max(road))
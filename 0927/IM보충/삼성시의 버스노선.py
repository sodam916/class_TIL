T = int(input())

for tc in range(1, T+1):
    N = int(input())
    line = [0] * 5001
    result = []
    for _ in range(N):
        a, b = map(int,input().split())
        for i in range(a, b+1):
            line[i] += 1
    P = int(input())
    for _ in range(P):
        c = int(input())
        result.append(line[c])

    print(f'#{tc}',*result)




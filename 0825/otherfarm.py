T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    m = (n - 1) // 2
    osr = n
    summ = 0

    for i in range(m+1):
        for num in range(-i, i+1):
            summ += arr[i][m + num]

    for j in range(m):
        for numm in range(-j, j+1):
            summ += arr[(n-1)-j][m + numm]

    print(f'#{tc}',summ)
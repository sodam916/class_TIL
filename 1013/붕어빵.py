T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    ans = 'possible'
    time = [0] * 11112

    for i in range(1,999):
        if (M * i) < 11112:
            time[M * i] += K

    for j in customer:
        if j < M:
            ans = 'impossible'
            break
        time[j] -= 1

    if sum(time[:customer[-1]+1]) < 0:
        ans = 'impossible'


    print(f'#{tc}',ans)


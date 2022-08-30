
import sys
sys.stdin = open("where_input.txt")

T = int(input())


for tc in range(1,T+1):
    N, K = map(int,(input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    maxv = 0
    ans = 0
    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
                if j == N-1:
                    result.append(cnt1)

            else:
                if cnt1 >= K:
                    result.append(cnt1)
                cnt1 = 0

    for j in range(N):
        cnt2 = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt2 += 1
                if i == N-1:
                    result.append(cnt2)

            else:
                if cnt2 >= K:
                    result.append(cnt2)
                cnt2 = 0
    for m in result:
        if m == K:
            ans += 1
    print(ans)
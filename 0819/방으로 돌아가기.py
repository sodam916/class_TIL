import sys
sys.stdin = open("room_input (1).txt")

T = int(input())

for tc in range(1, T + 1):
    cnt = [0] * 201
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = (a + 1) // 2, (b + 1) // 2     # 방번호를 1~200 부여
        if a > b:
            a, b = b, a

        for i in range(a, b+1):
            cnt[i] += 1

    ans = 0
    for val in cnt:
        if ans < val:
            ans = val
    print(f'#{tc}',ans)
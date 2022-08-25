import sys
sys.stdin = open("omok_input (1).txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for testcase in range(1, T + 1):
    n = int(input())
    arr = [list(map(str, input().strip())) for _ in range(n)]
    lst = []
    dr = [1, 1]  # 상하좌우
    dc = [-1, 1]
    sr = sc = 1
    ans = []

    for r in range(n):
        cnt = 0
        for c in range(n):
            if arr[r][c] == 'o':
                cnt += 1
                if cnt >= 5:
                    print('YES')
                    break
            else:
                cnt = 0


    for c in range(n):
        cnt = 0
        for r in range(n):
            if arr[r][c] == 'o':
                cnt += 1
                if cnt >= 5:
                    print('YES')
                    break
            else:
                cnt = 0

    for r in range(n):
        for c in range(n):
            for k in range(2):
                cnt = 0
                for q in range(5):
                    tr = r + (dr[k] * q)
                    tc = c + (dc[k] * q)
                    if 0 <= tr < n and 0 <= tc < n:
                        if arr[tr][tc] == 'o':
                            cnt += 1
                            if cnt >= 5:
                                print('YES')
                                break
                        else:
                            cnt = 0




    # for num in lst:
    #     if num >= 5:
    #         ans.append(1)
    #
    # if 1 in ans:
    #     print(f'#{testcase} YES')
    # else:
    #     print(f'#{testcase} NO')

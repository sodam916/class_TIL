# 가지치기

arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]


N = int(input())
cols = [i for i in range(N)]    # 열의 위치

def perm(k, cur_sum):
    global ans
    # if cur_sum >= ans:
    #     return

    if k == N:
        s = 0
        for j in range(N):
            s += arr[j][cols[j]]
        print(cols, s, cur_sum)
        if ans > s:
            ans = s
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]     # k 행의 열의 위치를 선택
            perm(k + 1, cur_sum + arr[k][(cols[k])])    # 이해 필요
            cols[k], cols[i] = cols[i], cols[k]

ans = 0xfffff
perm(0, 0)
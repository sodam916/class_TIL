import sys
sys.stdin = open('omok_input (1).txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input().strip())) for _ in range(N)]
    lst = []
    ans = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                lst.append(1)
            else:
                lst.append(0)
    for c in range(N):
        for r in range(N):
            if arr[r][c] == 'o':
                lst.append(1)
            else:
                lst.append(0)
    for i in range(N):
        if arr[i][i] == 'o':
            lst.append(1)
        else:
            lst.append(0)
    for i in range(N):
        if arr[i][N-i-1] == 'o':
            lst.append(1)
        else:
            lst.append(0)
    for n in range(0,len(lst)-N+1,N):
        summ = 0
        for m in range(0,N):
            summ += lst[n+m]

        ans.append(summ)

    for f in range(len(ans)):
        if ans[f] >= N:
            ans.append('y')
        else:
            ans.append('n')
    print(ans)
    if 'y' in ans:
        print('YES')
    else:
        print('NO')
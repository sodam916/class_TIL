import sys
sys.stdin = open("sudoku_input (1).txt")
T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = []

    # 가로 체크
    for i in range(9):
        checkr = 0
        for j in range(9):
            checkr += arr[i][j]
        if checkr == 45:
            ans.append(0)
    # 세로 체크
    for j in range(9):
        checkc = 0
        for i in range(9):
            checkc += arr[i][j]
        if checkc == 45:
            ans.append(0)

    for i in range(3):
        for j in range(3):
            check3 = 0
            for r in range(3):
                for c in range(3):
                    check3 += arr[r+(3*i)][c+(3*j)]
            if check3 == 45:
                ans.append(0)

    if len(ans) == 27:
        print(f'#{tc}','1')
    else:
        print(f'#{tc}','0')








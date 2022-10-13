T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    result = 'yes'

    x1 = y1 = N  # 좌측상단으로 만들것
    x2 = y2 = 0  # 우측하단으로 만들것

    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)


    # 끝이 #으로 된 사각형의 가로세로 같다면 정사각형, 그안에 .이 하나라도 있다면 X판정
    if x2 - x1 != y2 - y1:  # 가로세로 길이가 다르면 정사각형X
        result = 'no'

    else:  # 길이가 같을때   # 영역내에서 .이 있는지 확인
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if board[i][j] == '.':
                    result = 'no'

    print(f'#{test_case} {result}')
    #
    #



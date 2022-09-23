T = int(input())

for tc in range(1, T+1):
    table = [list(map(str, input().split())) for _ in range(4)]
    dr = [1, -1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    result = []
    number = ''
    def findnum(r, c, idx, number):
        number += table[r][c]
        if idx == 6:
            result.append(number)
            return
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                findnum(nr, nc, idx + 1, number)

    for r in range(4):
        for c in range(4):
            findnum(r, c, 0, '')
    ans = set(result)
    print(f'#{tc}',len(ans))

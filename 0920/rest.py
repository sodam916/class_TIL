

N, M = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(N)]
ans = []
#
# def findcode(x):
#     dr = [1] #우측

while True:
    for r in range(N):
        code = ''
        for g in range(M):
            if arr[r][g] != '0':
                if arr[r][g] == '0':
                    break
                else:
                    code += arr[r][g]
        ans.append(code)

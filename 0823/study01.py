
N = 5
tmp = []        # 현재까지 붙여진 종이
cnt = 0
def paper(n):   # 현재 종이 길이 = n
    if n > N: return
    if n == N:
        global cnt; cnt += 1
        print(*tmp)
        return
    else:
        tmp.append('ㅣ')
        paper(n + 1)
        tmp.pop()

        tmp.append('ㅁ')
        paper(n + 2)
        tmp.pop()

        tmp.append('=')
        paper(n + 2)
        tmp.pop()

paper(0)
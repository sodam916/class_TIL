p = 'CATTCCCT'
t = 'ATTTGTGCATGTTTCATTCCCT'

n, m = len(t), len(p)
# 텍스트에서 패턴이 존재할 수 있는 모든 시작위치
for i in range(n - m + 1): #0
    #i = 매칭할 텍스트의 시작 위치
    for j in range(m): #0 ~ m-1
        if p[j] != t[i + j]:
            break
    #for문에서 못잡으면 else로 옴
    else:
        print(i, t[i:i + m])
        break


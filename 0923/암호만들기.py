L, C = map(int, input().split())
alpha = list(map(str, input().split()))
necce = ['a', 'e', 'i', 'o', 'u']
visited = [0] * (C+1)
wordlst = []
result = []
alpha.sort()

def check(x):
    word = []
    cnt = 0
    for i in x:
        if i in necce:
            cnt += 1
    return cnt



def back(k,temp):
    if len(wordlst) == L:
        result.append(''.join(map(str, wordlst)))
        return
    else:
        for i in range(k, C):
            if visited[i] == 0:
                visited[i] = 1
                wordlst.append(alpha[i])
                back(i+1, temp)
                wordlst.pop()
                visited[i] = 0
back(0, [])

for i in result:
    if check(i) > 2:
        print(i)
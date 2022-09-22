arr = [0] * 9
s = []
visited = [0] * 9

for j in range(9):
    arr[j] = int(input())

all = sum(arr)
ans = []

def dfs(st):
    global visited
    if len(s) == 7:
        if sum(s) == 100:
            for m in sorted(s):
                ans.append(m)
        return
    for i in range(st, 9):
        if visited[i] == 0:
            visited[i] = 1
            s.append(arr[i])
            dfs(i+1)
            s.pop()
            visited[i] = 0
dfs(0)
for k in range(0,7):
    print(ans[k])

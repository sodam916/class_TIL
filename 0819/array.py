import sys
N, M = map(int,sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
sq = int(sys.stdin.readline())
arrsq = []
for i in range(sq):
    arrsq.append(list(map(int,sys.stdin.readline().split())))


for n in range(sq):
    summ = 0
    for i in range(arrsq[n][0]-1,arrsq[n][2]):
        for j in range(arrsq[n][1]-1,arrsq[n][3]):
            summ += arr[i][j]
    print(summ)




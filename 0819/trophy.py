n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, len(arr)):
    cnt1 = 0
    if arr[i-1][0] < arr[i][0]:
        cnt1 += 1
    else:
        print(cnt1)
# print(cnt1)

for j in range(len(arr)-1,0,-1):
    cnt2 = 0
    if arr[j-1][0] < arr[j][0]:
        cnt2 += 1
    else:
        print(cnt2)
    # print(j)
# print(cnt2)
arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(arr)

# (N-1) - i  + 밑에 깔리는 상자 개수 = 낙차
# 내 오른쪽에 같거나 같은 상자가 몇개

ans = 0
for i in range(N):
    #상자에서 벽까지
    height = N - 1 - i
    #밑에 깔리는 상자들의 개수 카운팅
    for j in range(i + 1, N):
        if arr[i] <= arr[j]:
            height -= 1
    if ans < height:
        ans = height

print(ans)





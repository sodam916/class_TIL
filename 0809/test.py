# N = int(input())
# arr = list(map(int, input().split()))
#
# tmp = [0] * N
# c = [0] * 101
# for i in range(N):
#     c[arr[i]] += 1
#
#
# for j in range(1,101): # 개수 누적
#     c[j] += c[j-1]
#
# for i in range(N-1, -1 ,-1): # 원본을 뒤에서부터 읽으면서 정렬 결과를 저장
#     c[arr[i]] -= 1
#     tmp[c[arr[i]]] = arr[i]
# print(tmp)



arr = [1, 2, 3, 4, 5, 6, 7, 8]
N = 8
M = 4

for s in range(0, N-M+1):
    print(s)
import sys
sys.stdin = open('input_view.txt')

N = int(input())
arr = list(map(int, input().split()))
for tc in (n):
    ans = 0
    for i in range(2, N-3 +1): #i 가 기준
        max_val = arr[i - 2]
        if max_val < arr[i - 1]:
            max_val = arr[i - 1]
        if max_val < arr[i + 1]:
            max_val = arr[i + 1]
        if max_val < arr[i + 2]:
            max_val = arr[i + 2]

        if arr[i] > max_val:
            ans += arr[i] - max_val
    print(ans)

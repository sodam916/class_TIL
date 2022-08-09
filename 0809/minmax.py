import sys
sys.stdin = open('minmax_input.txt')
T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = arr[0]
    min_val = arr[0]
    for val in arr:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
    print(f"#{tc+1}", max_val - min_val)
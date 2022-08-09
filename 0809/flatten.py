# import sys
# sys.stdin = open('input_dump.txt')


# for tc in range(1, 11):
N = int(input())
arr = list(map(int, input().split()))
max_val = arr[0] # 100
min_val = arr[0] # 1
while True:
    for maxx in arr:
        if max_val < maxx:
            max_val = maxx

    for min in arr:
        if min_val > min:
            min_val = min
    maxx - 1
    min + 1
    N - 1
    if N == 0:
        break
    print(maxx, min)

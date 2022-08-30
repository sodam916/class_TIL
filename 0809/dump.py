import sys
sys.stdin = open('input_dump.txt')
N = int(input())
arr = list(map(int, input().split()))

for tc in range(1, 11):

    max_idx = 0
    min_idx = 0
    max = 0
    min = 0
    b = 0
    while b < N:
        b += 1
        for a in range(len(arr)):
            if arr[max_idx] < arr[a]:
                max_idx = a
            if arr[min_idx] > arr[a]:
                min_idx = a
        arr[max_idx] -= 1
        arr[min_idx] += 1

        for b in range(len(arr)):
            if max < arr[b]:
                max = arr[b]
            if min > arr[b]:
                min = arr[b]

    print(max, min)



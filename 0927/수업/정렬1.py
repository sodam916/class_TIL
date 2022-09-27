def merge_arr(left_arr, right_arr):
    global answer
    if left_arr[-1] > right_arr[-1]:
        answer += 1
    merge_arr = []
    left_idx, right_idx = 0, 0
    n, m = len(left_arr), len(right_arr)

    while left_idx != n and right_idx != m:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merge_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merge_arr.append(right_arr[right_idx])
            right_idx += 1

    if left_idx != n:
        merge_arr += left_arr[left_idx:]
    if right_idx != m:
        merge_arr += right_arr[right_idx:]

    return merge_arr


def divide_arr(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = divide_arr(a[:mid])
    right = divide_arr(a[mid:])
    return merge_arr(left, right)
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = divide_arr(arr)
    answer = 0
    print(f'#{tc}',arr[N//2])
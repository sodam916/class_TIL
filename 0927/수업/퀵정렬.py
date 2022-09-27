
def quick_hoare(s, e):
    # 계속 갈지말지
    if s >= e:
        return
    # partition
    i, j = s, e
    p = arr[s]      # 피봇
    while i <= j:
        while i <= e and p >= arr[i]:
            i += 1
        while p < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    # 분할 위치는 피봇이 있는 j
    quick_hoare(s, j-1)
    quick_hoare(j+1, e)


arr = [69, 30, 10, 2, 16, 8, 32, 21]
quick_hoare(0, len(arr)-1)
print(arr)

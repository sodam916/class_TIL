def merge_sort(s, e):    # 구간정보 (시작, 끝)
    if s == e:
        return
    mid = (s + e) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)
    i, j, k = s, mid + 1, s

    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1
            k += 1
        else:
            tmp[k] = arr[j]
            j += 1
            k += 1
    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1
    while j <= e:
        tmp[k] = arr[j]
        j += 1
        k +=1

    for i in range(s, e+1):
        arr[i] = tmp[i]
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * len(arr)
    merge_sort(0, len(arr)-1)
    print(f'#{tc}',tmp[N//2])
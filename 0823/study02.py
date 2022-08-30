# 순열 생성

arr = [10, 20, 30, 40]    # 초기 상태
N = 4

for i in range(0, N):
    arr[0], arr[i] = arr[i], arr[0]
    # print(arr)
    # arr[0], arr[i] = arr[i], arr[0]  # 초기 상태로 다시 돌려놓기
    # ==========================================
    for n in range(1, N):
        arr[1], arr[i] = arr[i], arr[1]
        # print(arr)
        # arr[1], arr[i] = arr[i], arr[1]
        # ===========================================
        for k in range(2, N):
            arr[2], arr[k] = arr[k], arr[2]
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]
        # ==========================================
        arr[1], arr[i] = arr[i], arr[1]
    # ==========================================
    arr[0], arr[i] = arr[i], arr[0]





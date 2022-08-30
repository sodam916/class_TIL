#순열 만들기 재귀함수
arr = [10, 20, 30, 40]    # 초기 상태
N = 4

def perm(k):
    if k == N:
        print(arr)
        return
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(0)
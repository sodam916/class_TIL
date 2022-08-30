

T = int(input())

for tc in range(1, T + 1):
    arr = [0] * 5001 # 1번부터 5000
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())

        for i in range(A, B + 1):
            arr[i] += 1

    P = int(input())
    for _ in range(P):
        p = int(input())
        print(arr[p], end ='')
    print()


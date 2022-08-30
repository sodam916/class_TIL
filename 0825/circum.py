T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    Q = []
    mo = []

    for i in range(M):
        mo.append(arr[0])
        arr.pop(0)
        arr.append(mo[0])
        mo.pop()

    print(f'#{tc}',arr[0])


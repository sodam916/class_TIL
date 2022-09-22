def lotto(x):
    if len(order) == 6:
        print(*order)
        return
    for i in range(x, K):
        if used[i] == 0:
            used[i] = 1
            order.append(arr[i])
            lotto(i+1)
            order.pop()
            used[i] = 0




while True:
    number = list(map(int, input().split()))
    K = number[0]
    arr = number[1::]
    used = [0] * K
    order = []
    lotto(0)
    print()

    if number[0] == 0:
        break



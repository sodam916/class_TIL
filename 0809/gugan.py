import sys
sys.stdin = open('gugan_input.txt')
T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))

    c = [0] * (N+1)
    tmp = [0] * N

    for i in range(0, len(arr)):
        c[arr[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in range(len(tmp)-1, -1, -1):
        c[arr[i]] -= 1
        tmp[c[arr[i]]] = arr[i]

    print(tmp)




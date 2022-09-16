T = int(input())

def findroot(c):
    while P[c] != 0:
        c = P[c]
        lst.append(c)


for tc in range(1,T+1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    L = [0] * (V+1)
    R = [0] * (V+1)
    P = [0] * (V+1)
    lst = []
    ans = []
    for i in range(0, E*2, 2):
        p, c = arr[i], arr[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p

    # c = n2
    # while P[c] != 0:
    #     c = P[c]
    #     lst.append(c)

    # c2 = n2
    # while P[c2] != 0:
    #     c = P[c2]
    #     lst.append(c2)
    findroot(n1)
    findroot(n2)

    # print(L)
    # print(R)
    # print(P)
    print(lst)
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)

    for i in range(0, E * 2, 2):
        p, c = arr[i], arr[i+1]

        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
            P[c] = p

    

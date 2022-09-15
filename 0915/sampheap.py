T = int(input())

def enq(n):
    global hsize
    hsize += 1
    H[hsize] = n
    c = hsize
    p = c // 2
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c//2

# def pop():
#     global hsize
#     # empty ==> (hsize == 0)
#     ret = H[1]
#     H[1] = H[hsize]
#     hsize -= 1
#
#     p, c = 1, 2  # c: 왼쪽 자식
#
#     while c <= hsize:
#         if c + 1 <= hsize and H[c] > H[c + 1]:
#             c += 1
#         if H[p] <= H[c]:
#             break
#         H[p], H[c] = H[c], H[p]
#         p = c
#         c = p * 2
#
#     return ret



for tc in range(1, T+1):
    V = int(input())
    arr = list(map(int, input().split()))

    H = [0] * 1000
    hsize = 0
    tree = [0]
    ans = 0

    for val in arr:
        enq(val)

    ln = V

    while True:
        pn = ln//2
        if pn == 1:
            ans += H[pn]
            break
        else:
            ans += H[pn]
            ln = pn

    # while ln:  # 1(루트노드) // 2를 하면 0. 0은 false니까 자동으로 끝남
    #     pn = ln // 2
    #     ans += H[pn]
    #     ln = pn
    print(f'#{tc}',ans)
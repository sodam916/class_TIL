T = int(input())

def inorder(v):

    if v > N:
        return
    inorder(v * 2)
    ans.append(v)
    inorder(v * 2 + 1)


for tc in range(1, T+1):
    N = int(input())
    tree = []
    ans = [0]
    lst = [0] * (N + 1)
    for i in range(N+1):
        tree.append(i)

    inorder(1)
    num = 0
    for j in ans:
        lst[j] = num
        num += 1

    print(f'#{tc}', lst[1], lst[N//2])




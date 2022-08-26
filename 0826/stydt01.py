V, E = map(int,input().split())

arr = list(map(int,input().split()))

# 트리 저장
L = [0] * (V + 1)         # 왼쪽 컴포
R = [0] * (V + 1)         # 오른쪽
P = [0] * (V + 1)         # 부모

for i in range(0, E*2, 2):
    parent, child = arr[i], arr[i + 1]
    if L[parent] == 0:
        L[parent] = child
    else:
        R[parent] = child

    P[child] = parent

def inorder(v):
    if v == 0:
        return
    # 방문 전위 순회
    print(v, end=' ')
    inorder(L[v])
    # 방문 중위 순회
    # print(v, end=' ')
    inorder(R[v])
    # 방문 후위 순회

inorder(1)
T = int(input())
def combi(k, ans):
    if k == N:
        temp = [i for i in ans]
        S.append(sum(temp))
        return

    ans.append(worker[k])
    combi(k + 1, ans)
    ans.pop()
    combi(k + 1, ans)


for tc in range(1, T+1):
    N, B = map(int, input().split())
    worker = list(map(int, input().split()))
    S = []
    result = []

    combi(0,[])
    for j in S:
        if j >= B:
            result.append(abs(j-B))

    print(f'#{tc}',min(result))


T = int(input())

for tc in range(1, T+1):
    card = list(map(int, input().split()))
    N = 12
    p1 = [0] * 10
    p2 = [0] * 10
    ans = 0

    for i in range(N):
        if i % 2 == 0:
            p1[card[i]] += 1
            if i >= 4:
                for s in range(8):
                    if p1[s] > 0 and p1[s + 1] > 0 and p1[s + 2] > 0:
                        ans = 1
                        break

                for e in range(10):
                    if p1[e] >= 3:
                        ans = 1
                        break

        else:
            p2[card[i]] += 1
            if i >= 5:
                for s in range(8):
                    if p2[s] > 0 and p2[s + 1] > 0 and p2[s + 2] > 0:
                        ans = 2
                        break

                for e in range(10):
                    if p2[e] >= 3:
                        ans = 2
                        break
        if ans != 0:
            break

    print(f'#{tc}',ans)
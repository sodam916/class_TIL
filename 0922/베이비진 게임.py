T = int(input())

for tc in range(1, T+1):
    card = list(map(int, input().split()))
    N = 12
    p1 = [0] * 10
    p2 = [0] * 10

    i = 0
    while True:
        if i == N:
            print(f'#{tc}', 0)
            break

        elif i % 2 == 0:
            p1[card[i]] += 1
            if i >= 4:
                for s in range(8):
                    if p1[s] > 0 and p1[s + 1] > 0 and p1[s + 2] > 0:
                        print(f'#{tc}', 1)
                        i += 1
                        break

                for e in range(10):
                    if p1[e] >= 3:
                        print(f'#{tc}', 1)
                        i += 1
                        break

        elif i % 2 != 0:
            p2[card[i]] += 1
            if i >= 4:
                for s in range(8):
                    if p2[s] > 0 and p2[s + 1] > 0 and p2[s + 2] > 0:
                        print(f'#{tc}', 1)
                        i += 1
                        break

                for e in range(10):
                    if p1[e] == 3:
                        print(f'#{tc}', 1)
                        i += 1
                        break






T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = round(n ** (1/3), 5)

    if a % 1 != 0:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}',int(a))
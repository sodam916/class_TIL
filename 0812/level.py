import sys
sys.stdin = open("level_input.txt")


T = int(input())

for tc in range(1, T+1):
    arr = list(map(str, input().split()))

    for i in arr:
        wl = list(i)
        num = len(wl)
        for n in range(num//2):
            wl[n], wl[num-1-n] = wl[num-1-n], wl[n]
        if i != (''.join(wl)):
            print(f"#{tc}", '0')
        else:
            print(f"#{tc}", '1')

        ans = 1
        for n in range(num//2):
            if wl[n] != wl[num-1-n]:
                ans = 0
                break

        print(f"#{tc}", ans)

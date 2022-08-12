import sys
sys.stdin = open("mirror_input.txt")


T = int(input())

for tc in range(1, T+1):
    arr = list(map(str, input().split()))

    for i in arr:
        wl = list(i)
        num = len(wl)
        for n in range(num//2):
            wl[n], wl[num-1-n] = wl[num-1-n], wl[n]

        for a in range(num):
            if wl[a] == 'b':
                wl[a] = 'd'
            elif wl[a] == 'd':
                wl[a] = 'b'
            elif wl[a] == 'p':
                wl[a] = 'q'
            elif wl[a] == 'q':
                wl[a] = 'p'


        print(f"#{tc}",''.join(wl))
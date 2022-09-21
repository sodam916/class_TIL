T = int(input())

for tc in range(1, T+1):

    le, number = map(str,input().split())


    m = len(number)
    ans = []
    p = 0
    for j in number:
        p += 1
        if j == 'A':
            j = 10
        elif j == 'B':
            j = 11
        elif j == 'C':
            j = 12
        elif j == 'D':
            j = 13
        elif j == 'E':
            j = 14
        elif j == 'F':
            j = 15
        four = []
        while True:
            a = int(j) // 2
            b = int(j) % 2
            four.insert(0, b)
            if a != 0:
                j = a
            else:
                break

        if len(four) < 4:
            for n in range(4-len(four)):
                four.insert(0,0)

        for m in four:
            ans.append(m)


    print(f'#{tc}',''.join(map(str,ans)))

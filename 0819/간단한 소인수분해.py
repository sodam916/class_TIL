T = int(input())
for tc in range(1,T+1):

    x = int(input())

    d = 2
    lst = []
    number = [0] * 12

    while d <= x:
        if x % d == 0:
            lst.append(d)
            x = x / d
        else:
            d = d + 1

    for num in lst:
        number[num] += 1

    print(f"#{tc}", number[2], number[3], number[5], number[7], number[11])




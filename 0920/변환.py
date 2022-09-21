T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # number = [input() for _ in range(N)]
    row = end = 0
    real = []
    ans = 0
    start = 0
    pwd = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    pwdlst = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    number = '01101000101101000110110111011011100100110100011011110100'
    for st in range(0, len(number)):
        if number[st:st + 7] in pwdlst:
            start = st
            break

    for m in range(start, len(number)-start, 7):
        print(pwd[number[m:m + 7]])


    # odd = real[0] + real[2] + real[4] + real[6]
    # even = real[1] + real[3] + real[5] + real[7]
    #
    # ans = odd * 3 + even
    #
    # if ans % 10 == 0:
    #     print(f'#{tc}', odd + even)
    # else:
    #     print(f'#{tc}', 0)
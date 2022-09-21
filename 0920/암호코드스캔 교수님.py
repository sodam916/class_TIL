T = int(input())

for tc in range(1, T+1):
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                }
    pwd = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    N, M = map(int, input().split())

    line_set = set()
    for _ in range(N):
        t = input().rstrip('0')
        if t:
            line_set.add(t)


    for line in line_set:
        i = len(line) - 1
        while i >= 55:
            if line[i] == '1':
                for _ in range(8):
                 # 8번 반복하며 0과 1 패턴 찾기
                    c1, c2, c3, c4 = 0
                    while line[i] == '1': c4 += 1; i -= 1
                    while line[i] == '0': c3 += 1; i -= 1
                    while line[i] == '1': c2 += 1; i -= 1
                    while line[i] == '0': c1 += 1; i -= 1
                    c1 = 7 - (c2+ c3+ c4)
                    i -= c1                 

                    #1의 개수 카운팅
            i -= 1

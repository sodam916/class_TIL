T = int(input())

for tc in range(1, T+1):
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                }
    pwd = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    pwdlst = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    N, M = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(N)]
    all = []
    row = end = 0
    ans = []
    code2 = []
    finalans = []
    for r in range(N):
        code = ''
        for g in range(M - 1):
            if arr[r][g] != '0':
                if arr[r][g + 1] == '0':
                    code += arr[r][g]
                    break
                else:
                    code += arr[r][g]
        all.append(code)

    set_all = set(all)
    all = list(set_all)


    for n in range(1, len(all)):
        numcode = ''
        for m in all[n]:
            numcode += hex_dict[m]
        code2.append(numcode)

    for cod in code2:
        tran = []
        before = []
        start = 0
        for st in range(0, len(cod)):
            if cod[st:st+7] in pwdlst:
                start = st
                break

        for mm in range(start, len(cod)-(len(cod)-56-start), 7):
            before.append(cod[mm:mm + 7])
        for be in range(len(before)):
            if len(before[be]) != 7:
                before.pop(be)

        for bee in before:
            tran.append(pwd[bee])
        ans.append(tran)


    print(ans)
    for l in ans:
        odd = even = 0
        if len(l) != 0:
            for aa in range(len(l)-1):
                if aa % 2 != 0:
                    even += l[aa]
                else:
                    odd += l[aa]


        final = odd * 3 + even + l[-1]
        print(final)
        if final % 10 == 0:
            finalans.append(odd + even + l[-1])

    if finalans is not []:
        print(f'#{tc}',*finalans)
    else:
        print(f'#{tc}', '0')









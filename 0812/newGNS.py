import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())
nums = 'ZRO'
for tc in range(1, T+1):
    m = 3
    tcn, ml = list(map(str, input().split()))
    arr = input().split()
    arrlist = ''
    p = int(ml)
    sword = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ans = []

    for word in arr:
        arrlist += word

    for search in sword:
        for i in range(len(arr)):
            for j in range(m):
                if search[j] != arrlist[i + j]:
                    break
            else:
                ans.append(arrlist[i:i + m])

    print(f'{tcn}')
    print(*ans)

import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())

for tc in range(1, T + 1):
    tcn, ml = list(map(str, input().split()))
    arr = input().split()
    arrlist = ''
    search = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ans = []

    for i in range(len(search)):
        for j in range(len(arr)):
            if search[i] == arr[j]:
                ans.append(arr[j])
    print(f'#{tc}')
    print(*ans)

    # for word in arr:
    #     arrlist += word
    # print(arrlist)

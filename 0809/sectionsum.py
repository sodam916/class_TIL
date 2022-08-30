import sys
sys.stdin = open('section_input.txt')
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_val = -999999
    min_val = 999999999

    # lists = [0] * N
    for s in range(0, N - M + 1):
        e = s + M - 1
        sums = 0
        for i in range(s, e+1):
            sums = sums + arr[i]
        if max_val < sums: max_val = sums
        if min_val > sums: min_val = sums

    print(max_val - min_val)




    # for j in lists[:-(M-1)]:
    #
    #     print(j)

        # max_val = arr[i-1] + arr[i] + arr[i+1]
        #
        # if max_val < arr[i] + arr[i+1] + arr[i+2]:
        #     max_val = arr[i] + arr[i+1] + arr[i+2]
        #
        # if max_val < arr[i+1] + arr[i+2] + arr[i+3]:
        #     max_val = arr[i+1] + arr[i+2] + arr[i+3]
        #
        # print(max_val)
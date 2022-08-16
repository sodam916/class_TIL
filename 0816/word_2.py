import sys
sys.stdin = open("word_2_input.txt")
T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    n = len(str1)
    m = len(str2)

    i = j = 0

    while i < n and j < m:
        if str1[i] == str2[j]:
            i, j = i + 1, j + 1
        else:
            j = j - i + 1
            i = 0
    if i == n:
        print(1)
    else:
        print(0)



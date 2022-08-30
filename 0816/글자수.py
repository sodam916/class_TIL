import sys
sys.stdin = open("글자수_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cstr = set(str1)
    strl = list(cstr)
    dic = {}
    ans = []
    for i in str2:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in strl:
        if i in dic:
            ans.append(dic.get(i))

    maxv = 0
    for j in ans:
        if maxv < j:
            maxv = j

    print(maxv)
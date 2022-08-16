import sys
sys.stdin = open("word_input.txt")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(N)]
    lst1 = []
    lst2 = []
    words = []
    words2 = []
    com = []
    com2 = []
    R = N*M
    for r in range(N):
        for j in range(N):
            lst1.append(arr[r][j])
    for s in range(0, R - M + 1):
        e = s + M - 1
        for i in range(s, s + M):
            words.append(lst1[i])
            com.append(lst1[i])
        for n in range(M // 2):
            words[n], words[M-n-1] = words[M-n-1], words[n]
        if com == words:
            print(f"#{tc}",''.join(com))
            break
        else:
            com = []
            words = []

    for r in range(N):
        for j in range(N):
            lst2.append(arr[j][r])
    for s in range(0, R - M + 1):
        e = s + M - 1
        for i in range(s, s + M):
            words2.append(lst2[i])
            com2.append(lst2[i])
        for n in range(M // 2):
            words2[n], words2[M-n-1] = words2[M-n-1], words2[n]
        if com2 == words2:
            print(f"#{tc}",''.join(com2))
            break
        else:
            com2 = []
            words2 = []
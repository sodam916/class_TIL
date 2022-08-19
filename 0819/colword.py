T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input().strip())) for _ in range(5)]

    for i in range(5):
        for j in range(5):
            print(arr[i][j])
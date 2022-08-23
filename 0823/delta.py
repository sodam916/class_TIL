arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dx = [0, 0, -1, 1]    # 상 하 좌 우
dy = [-1, 1, 0, 0]
delt_diagonal = [[-1, -1], [-1, 1], [1, -1], [1, 1]]    # 좌상 우상 좌하 우하
x = 1
y = 1
for i in range(4):
    pointx = x + dx[i]
    pointy = y + dy[i]

    print(arr[pointx][pointy])

for j in range(4):
    diagx = x + delt_diagonal[j][0]
    diagy = y + delt_diagonal[j][1]

    print(arr[diagx][diagy])


A, B = map(int,input().split())
result = []
summ = 0
for i in range(B):
    for j in range(i):
        result.append(i)


print(sum(result[A-1:B]))


# for n in range(A-1,B):
#     summ += result[n]
#
# print(summ)
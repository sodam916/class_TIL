p = 'CATTCCCT'
t = 'ATTTGTGCATGTTTCATTCCCT'

n, m = len(t), len(p)

i = j = 0
while i < n and j < m:
    # 일치하는 경우
    if p[j] == t[i]:
        i, j = i +1, j+1
    # 불일치하는 경우
    else:
        i = i - j + 1
        j = 0

if j == m:
    print(t[ i- m : i])

# while i < n and j < m:
#     # 일치하는 경우
#     if p[j] == t[i]:
#         i = i - j
#         j = -1
#
#     i, j = i + 1, j + 1
#     # 불일치하는 경우
#
# if j == m:
#
#     print(t[i - m: i])
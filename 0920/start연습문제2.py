number = '416A676F725974684D2050726F626C656D20536F6C76696E6'
n = int(number, 16)
ans = ''
#
# while True:
#     a = int(n // 2)
#     b = int(n % 2)
#
#     ans.insert(0, b)
#     if a != 0:
#         n = a
#     else:
#         break
#
# final = ''.join(map(str, ans))

while n > 0:
    a = n % 2
    n = n // 2
    ans = str(a)+ans

print(ans)

#
# def strlen(arr):
#     i = 0
#     while arr[i] != '\0':
#         i += 1
#     return i
#
#
#
#
# arr = ['s', 's', 'a', 'f', 'y', '\0']
#
# print(strlen(arr))



mystr ='algorithm'
# #1
# print(mystr[::-1])
#
# #2
# revs = ''
# for i in range(len(mystr) -1, -1, -1):
#     revs += mystr[i]
# print(revs)

#3
# arr = list(mystr)
# N = len(arr)
# for i in range(N // 2):
#     # i <==> N -1-i
#     arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
#
# print(arr)
# print(''.join(arr))
# print(*arr)
#

s1 = 'abc'
s2 = 'abc'

print(s1 is s2, s1 == s2)




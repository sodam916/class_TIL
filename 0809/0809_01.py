
arr = [55, 7, 78, 12, 42]

# max_val = arr[0]
#
# for val in arr:
#     if max_val < val:
#         max_val = val


# max_idx = 0
# min_idx = 0
# for i in range(1, len(arr)):
#     if arr[max_idx] < arr[i]:
#         max_idx = i
#     if arr[min_idx] > arr[i]:
#         min_idx = i
#
# print(arr[min_idx], arr[max_idx])
min_idx = 0
cnt = 0
for i in range(1, len(arr)):
    if arr[min_idx] > arr[i]:
        min_idx = i
        cnt = 1
    elif arr[min_idx] == arr[i]:
        cnt += 1

print(arr[min_idx], cnt)
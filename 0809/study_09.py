'''
합이 0이 되는 3개의 엘리먼트 출력
'''


nums = [-1, 0, 1, 2, -1, -4]

R = 0
l = 0
r = len(nums) - 1
for i in nums:
    while l <= r: # 두 포인터의 기준을 잡아줌
        if nums[l] + nums[r] > R - i:
            r -= 1
        elif nums[l] + nums[r] < R - i:
            r += 1
        elif nums[l] + nums[r] == R - i:
            print(nums[l], nums[r], i)
            r -= 1
            l += 1




# for i in nums:
#     other = 0 - i
#     for j in range(len(nums)):
#         ans = []
#         if nums[j] + nums[j+1] == other:


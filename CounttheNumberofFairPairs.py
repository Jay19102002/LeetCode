# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

def countFairPairs(nums, lower, upper):
    nums.sort()
    l, r, res = 0,0,0
    for i in range(len(nums)-1, 0, -1):
        if nums[i] + nums[i-1] < lower:
            break
        if nums[i] + nums[l] > upper:
            continue
        while r < i and nums[r] + nums[i] <= upper:
            r += 1
        if r == i or nums[r] + nums[i] > upper:
            r -= 1
        while l <= r and nums[l] + nums[i] < lower:
            l += 1
        if l <= r:
            res += r-l+1
    return res

nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
print(countFairPairs(nums, lower, upper))  
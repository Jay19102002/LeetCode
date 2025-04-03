# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 

def largestTripleProduct(nums):
    maxi = float('-inf')
    diff = 0
    res = 0
    
    for i in range(len(nums)):
        maxi = max(maxi, nums[i])
        if i >= 2:
            res = max(res, diff * nums[i])
        if i >= 1:
            diff = max(diff, maxi - nums[i])
            
    return res

nums = [12,6,1,2,7]
print(largestTripleProduct(nums))  
# Input: nums = [1,2,1,4,1]

# Output: 1

# Explanation:

# Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

def countSubarrays(nums):
    count = 0
    n = len(nums)
    
    for i in range(1, n - 1):
        if nums[i - 1] + nums[i + 1] == nums[i] / 2:
            count += 1
    
    return count

nums = [1, 2, 1, 4, 1]
print(countSubarrays(nums))  
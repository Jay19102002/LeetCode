# Input: nums = [12,6,1,2,7]
# Output: 77
# Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
# It can be shown that there are no ordered triplets of indices with a value greater than 77. 

def maximumValue(nums):
    n = len(nums)
    max_value = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
    return max_value

nums = [12,6,1,2,7]
print(maximumValue(nums)) 
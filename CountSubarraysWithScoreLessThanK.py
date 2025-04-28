# Input: nums = [2,1,4,3,5], k = 10
# Output: 6
# Explanation:
# The 6 subarrays having scores less than 10 are:
# - [2] with score 2 * 1 = 2.
# - [1] with score 1 * 1 = 1.
# - [4] with score 4 * 1 = 4.
# - [3] with score 3 * 1 = 3. 
# - [5] with score 5 * 1 = 5.
# - [2,1] with score (2 + 1) * 2 = 6.
# Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.

def countSubarrays(nums, k):
    start = 0
    sum_ = 0
    count = 0
    
    for end in range(len(nums)):
        sum_ += nums[end]
        
        while sum_ * (end - start + 1) >= k:
            sum_ -= nums[start]
            start += 1
        
        count += (end - start + 1)
    
    return count

nums = [2, 1, 4, 3, 5]
k = 10
print(countSubarrays(nums, k)) 
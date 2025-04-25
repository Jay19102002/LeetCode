# Input: nums = [3,2,4], modulo = 2, k = 1
# Output: 3
# Explanation: In this example the interesting subarrays are: 
# The subarray nums[0..0] which is [3]. 
# - There is only one index, i = 0, in the range [0, 0] that satisfies nums[i] % modulo == k. 
# - Hence, cnt = 1 and cnt % modulo == k.  
# The subarray nums[0..1] which is [3,2].
# - There is only one index, i = 0, in the range [0, 1] that satisfies nums[i] % modulo == k.  
# - Hence, cnt = 1 and cnt % modulo == k.
# The subarray nums[0..2] which is [3,2,4]. 
# - There is only one index, i = 0, in the range [0, 2] that satisfies nums[i] % modulo == k. 
# - Hence, cnt = 1 and cnt % modulo == k. 
# It can be shown that there are no other interesting subarrays. So, the answer is 3.

def countInterestingSubarrays(nums, modulo, k):
    prefixModCount = {0: 1}
    prefixSum = 0
    result = 0
    
    for num in nums:
        if num % modulo == k:
            prefixSum += 1
        remainder = prefixSum % modulo
        target = (remainder - k) % modulo
        result += prefixModCount.get(target, 0)            
        prefixModCount[remainder] = prefixModCount.get(remainder, 0) + 1
    
    return result   

nums = [3, 2, 4]
modulo = 2
k = 1
print(countInterestingSubarrays(nums, modulo, k)) 
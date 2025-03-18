# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.

def longestNiceSubarray(nums ):
    ans = 0
    B = 0
    l = 0
    for r,x in enumerate(nums):
        while l < r and (B & x)!=0:
            B^= nums[l]
            l+=1
        B |= x
        ans = max(ans,r-l+1)
    return ans

nums = [1,3,8,48,10]
print(longestNiceSubarray(nums)) 
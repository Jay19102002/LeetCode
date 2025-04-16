# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.


from collections import defaultdict

def countGood(nums, k):
    n = len(nums)
    freq = defaultdict(int)
    ans, count, l = 0,0,0
    for r,x in enumerate(nums):
        count += freq[x]
        freq[x] += 1
        while count >= k:
            ans += n-r
            freq[nums[l]] -= 1
            count -= freq[nums[l]]
            l+=1
    return ans

nums = [3,1,4,3,2,2,4]
k = 2
print(countGood(nums, k))  
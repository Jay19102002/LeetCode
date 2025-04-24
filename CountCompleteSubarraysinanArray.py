# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

from collections import defaultdict

def countCompleteSubarrays(nums):
    total_distinct = len(set(nums))
    count = defaultdict(int)
    left = res = 0
    for right in range(len(nums)):
        count[nums[right]] += 1
        while len(count) == total_distinct:
            res += len(nums) - right
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
    return res

nums = [1, 3, 1, 2, 2]
print(countCompleteSubarrays(nums))  
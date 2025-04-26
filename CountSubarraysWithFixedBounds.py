# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

def countSubarrays(nums, minK, maxK):
    n = len(nums)
    count = 0
    left = 0
    minIndex = -1
    maxIndex = -1

    for right in range(n):
        if nums[right] < minK or nums[right] > maxK:
            left = right + 1
            minIndex = -1
            maxIndex = -1
        if nums[right] == minK:
            minIndex = right
        if nums[right] == maxK:
            maxIndex = right

        count += max(0, min(minIndex, maxIndex) - left + 1)

    return count

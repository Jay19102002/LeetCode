# Input: nums = [5,2,5,4,5], k = 2

# Output: 2

# Explanation:

# The operations can be performed in order using valid integers 4 and then 2.

def minOperations(nums, k):
    if k > min(nums):
        return -1

    elements = set(nums)
    count = len(elements)

    if k in elements:
        return count - 1
    else:
        return count

nums = [5,2,5,4,5]
k = 2
print(minOperations(nums, k))  
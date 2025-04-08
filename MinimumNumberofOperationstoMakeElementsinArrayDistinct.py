# Input: nums = [1,2,3,4,2,3,3,5,7]

# Output: 2

# Explanation:

# In the first operation, the first 3 elements are removed, resulting in the array [4, 2, 3, 3, 5, 7].
# In the second operation, the next 3 elements are removed, resulting in the array [3, 5, 7], which has distinct elements.
# Therefore, the answer is 2.

def minimumOperations(nums):
    count = 0
    while len(nums)>len(set(nums)):
        nums = nums[3:]
        count += 1
    return count

nums = [1,2,3,4,2,3,3,5,7]
print(minimumOperations(nums))  
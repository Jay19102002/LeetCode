# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following: 
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.

def minOperations( grid, x):
    nums = [num for row in grid for num in row]
    mod = nums[0] % x
    if any(num % x!= mod for num in nums):
        return -1
    
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) // x for num in nums)

grid = [[2,4],[6,8]]
x = 2
print(minOperations(grid, x))  
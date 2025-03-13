# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

# Output: 2

# Explanation:

# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

def minZeroArray( nums, queries):
    n = len(nums)
    m = len(queries)
    diff = [0]*(n+1)
    curr_sum = j = 0
    for i,num in enumerate(nums):
        curr_sum += diff[i]
        while j < m and curr_sum < num:
            l, r, val = queries[j]
            j += 1
            
            if i < l:
                diff[l] += val
            elif i <= r:
                curr_sum += val
            
            diff[r+1] -= val
        if curr_sum < num:
            return -1
    return j

nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
print(minZeroArray(nums, queries))  
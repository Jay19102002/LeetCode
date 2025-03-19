# Input: nums = [0,1,1,1,0,0]

# Output: 3

# Explanation:
# We can do the following operations:

# Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
# Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
# Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

def minOperations(nums):
    k = 0
    for i in range(len(nums) - 2):
        if nums[i] == 0:
            nums[i] ^= 1
            nums[i+1] ^= 1
            nums[i+2] ^= 1
            k+=1
    return -1 if 0 in nums else k

nums = [0,1,1,1,0,0]
print(minOperations(nums))
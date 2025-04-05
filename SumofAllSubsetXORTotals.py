# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6

def xorSum(nums):
    # Initialize the total sum to 0
    total_sum = 0

    # Iterate through each number in the input list
    for num in nums:
        # Calculate the XOR of the current number with itself and add it to the total sum
        total_sum |= num
        
    return total_sum * (1 << (len(nums) - 1))

nums = [1,3]
print(xorSum(nums))  
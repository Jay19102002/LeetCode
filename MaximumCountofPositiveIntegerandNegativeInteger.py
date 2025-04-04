# Example 1:
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 2:
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 3:
# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

def maxCount(nums):
    positive = []
    negative = []

    for num in nums:
        if num > 0:
            positive.append(num)
        elif(num < 0):
            negative.append(num)

    res = max(len(positive),len(negative))

    return res

nums = [-3,-2,-1,0,0,1,2]
print(maxCount(nums))  
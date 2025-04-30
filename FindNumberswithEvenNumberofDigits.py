# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

def findNumbers(nums):
    # Initialize a counter for numbers with an even number of digits
    count = 0
    
    # Traverse each number in the list
    for num in nums:
        # Convert the number to string and check if its length is even
        if len(str(num)) % 2 == 0:
            count += 1
    
    return count

nums = [12, 345, 2, 6, 7896]
print(findNumbers(nums))  
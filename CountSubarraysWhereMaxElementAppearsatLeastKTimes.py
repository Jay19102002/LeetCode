# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

def countSubarrays(nums, k):
    result = 0
    left = 0
    maxValue = max(nums)
    
    for num in nums:
        if num == maxValue:
            k -= 1
        while k ==0:
            if nums[left] == maxValue:
                k += 1
            left += 1
            
        result += left
        
    return result        

nums = [1, 3, 2, 3, 3]
k = 2
print(countSubarrays(nums, k)) 
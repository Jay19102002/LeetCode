# Input: nums = [1,2,2,2]
# Output: 2
# Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
# In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
# In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
# Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
# It can be shown that index 2 is the minimum index of a valid split. 

def minIndex(nums):
    def find_dominant_element(arr):
        candidate = None
        count = 0
            
        # Boyer-Moore Majority Vote algorithm
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
            
        count = sum(1 for num in arr if num == candidate)
        return candidate if count > len(arr) // 2 else None

    dominant = find_dominant_element(nums)
    
    if dominant is None:
        return -1
        
    left_count = 0
    total_dominant_count = sum(1 for num in nums if num == dominant)
        
    for i in range(len(nums) - 1):
        if nums[i] == dominant:
            left_count += 1
            
        left_subarray_count = left_count
        right_subarray_count = total_dominant_count - left_count
            
        if (left_subarray_count > (i + 1) // 2 and 
            right_subarray_count > (len(nums) - i - 1) // 2):
            return i
        
    return -1
    
# Time complexity: O(n)
# Space complexity: O(1)
nums = [1,2,2,2]
print(minIndex(nums))  
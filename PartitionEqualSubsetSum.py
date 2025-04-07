# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

def canPartition(nums):
    sum1=sum(nums)
    if sum1&1: 
        return False
    K=sum1//2
     
    def f(i, sum1):
        if sum1==K: return True
        if i<0 or sum1>K: return False
        return f(i-1, sum1+nums[i]) or f(i-1, sum1)
        
    return f(len(nums)-1, 0)

nums = [1,5,11,5]
print(canPartition(nums))  
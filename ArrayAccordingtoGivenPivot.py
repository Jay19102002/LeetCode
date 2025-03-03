# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]
# Explanation: 
# The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
# The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
# The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

def arrayPivot():
    less = []
    equal = []
    greater = []
    for i in nums:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    
    less.extend(equal)
    less.extend(greater)
    return less

nums = [9,12,5,10,14,3,10]
pivot = 10
print(arrayPivot())  
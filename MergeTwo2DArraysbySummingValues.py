# Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
# Output: [[1,6],[2,3],[3,2],[4,6]]
# Explanation: The resulting array contains the following:
# - id = 1, the value of this id is 2 + 4 = 6.
# - id = 2, the value of this id is 3.
# - id = 3, the value of this id is 2.
# - id = 4, the value of this id is 5 + 1 = 6.

def merge(nums1,nums2):
    map = {}
    for i in range(len(nums1)):
        map[nums1[i][0]] = nums1[i][1]
    
    for i in range(len(nums2)):
        if nums2[i][0] in map:
            map[nums2[i][0]] += nums2[i][1]
        else:
            map[nums2[i][0]] = nums2[i][1]
    return list(map.items())

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(merge(nums1,nums2))
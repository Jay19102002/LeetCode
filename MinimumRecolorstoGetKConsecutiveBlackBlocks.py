# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

# Example 2:
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.

#sliding window approach
def minRecolors(blocks,k):
    wcount = 0
    for i in range(k):
        if blocks[i] == 'W':
            wcount += 1
            
    count = wcount
    for i in range(k,len(blocks)):
        if blocks[i-k]=='W':
            wcount-=1
        if blocks[i]=='W':
            wcount+=1
        count = wcount if wcount < count else count
    return count

blocks = "WBBWWBBWBW"
k = 2
print(minRecolors(blocks,k))  
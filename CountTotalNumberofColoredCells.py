# Example 1:

# Input: n = 1
# Output: 1
# Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
# Example 2:

# Input: n = 2
# Output: 5
# Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 

def coloredCells(n):
        return 2*n*(n-1)+1

minute = 2
print(coloredCells(minute))  # Output: 5
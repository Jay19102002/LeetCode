# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
# Example 2:

# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].

def missAndRepeat(grid):
    count = {}
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in count:
                count[grid[i][j]] = 1
            else:
                count[grid[i][j]] += 1
    repeat = missing = 0
    for num in range(1,n*n + 1):
        if num not in count:
            missing = num
        elif count[num] == 2:
            repeat = num
    return [repeat,missing]

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(missAndRepeat(grid)) 
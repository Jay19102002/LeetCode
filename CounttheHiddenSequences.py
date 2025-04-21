# Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
# Output: 4
# Explanation: The possible hidden sequences are:
# - [-3, 0, -4, 1, 2, 0]
# - [-2, 1, -3, 2, 3, 1]
# - [-1, 2, -2, 3, 4, 2]
# - [0, 3, -1, 4, 5, 3]
# Thus, we return 4.

def countHiddenSequences(differences, lower, upper):
    min_sum = 0
    max_sum = 0
    current_sum = 0

    for diff in differences:
        current_sum += diff
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)

    # Calculate the range of possible starting values
    start_min = lower - min_sum
    start_max = upper - max_sum

    # The number of valid starting values is the range between start_min and start_max
    return max(0, start_max - start_min + 1)

differences = [3, -4, 5, 1, -2]
lower = -4
upper = 5
print(countHiddenSequences(differences, lower, upper))  
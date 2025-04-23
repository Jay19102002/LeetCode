# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

def countLargestGroup(n: int) -> int:
    def digit_sum(num: int) -> int:
        return sum(int(digit) for digit in str(num))

    group_count = {}
    for i in range(1, n + 1):
        s = digit_sum(i)
        if s in group_count:
            group_count[s] += 1
        else:
            group_count[s] = 1

    max_size = max(group_count.values())
    return sum(1 for count in group_count.values() if count == max_size)

print(countLargestGroup(13))
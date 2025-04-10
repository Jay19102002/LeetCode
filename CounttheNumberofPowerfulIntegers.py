# Input: start = 1, finish = 6000, limit = 4, s = "124"
# Output: 5
# Explanation: The powerful integers in the range [1..6000] are 124, 1124, 2124, 3124, and, 4124. All these integers have each digit <= 4, and "124" as a suffix. Note that 5124 is not a powerful integer because the first digit is 5 which is greater than 4.
# It can be shown that there are only 5 powerful integers in this range.

def numberOfPowerfulInt(start, finish, limit, suffix):
    def count_powerful_up_to(num):
        num_str = str(num)
        suffix_len = len(suffix)
        prefix_len = len(num_str) - suffix_len
        if prefix_len < 0:
            return 0
        dp = [[0] * 2 for _ in range(prefix_len + 1)]
        dp[prefix_len][0] = 1
        suffix_from_num = num_str[prefix_len:]
        dp[prefix_len][1] = int(suffix_from_num) >= int(suffix)
        for i in range(prefix_len - 1, -1, -1):
            digit = int(num_str[i])
            dp[i][0] = (limit + 1) * dp[i + 1][0]
            if digit <= limit:
                dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
            else:
                dp[i][1] = (limit + 1) * dp[i + 1][0]
        return dp[0][1]
    return count_powerful_up_to(finish) - count_powerful_up_to(start - 1)

start = 1
finish = 6000
limit = 4
suffix = "124"
print(numberOfPowerfulInt(start, finish, limit, suffix))  
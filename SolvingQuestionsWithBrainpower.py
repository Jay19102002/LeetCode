# Input: questions = [[3,2],[4,3],[4,4],[2,5]]
# Output: 5
# Explanation: The maximum points can be earned by solving questions 0 and 3.
# - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
# - Unable to solve questions 1 and 2
# - Solve question 3: Earn 2 points
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

def mostPoints(questions):
    n = len(questions)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1 ,-1):
        points = questions[i][0]
        brainpower = questions[i][1]
        next = i + brainpower + 1
        take = points + (dp[next] if next < n else 0)
        skip = dp[i + 1]
        dp[i] = max(take, skip)
    return dp[0]
    
questions = [[3,2],[4,3],[4,4],[2,5]]
print(mostPoints(questions)) 
# Input: nums = [8,3,9,3,8], k = 2
# Output: 81
# Explanation: To get a score of 81, we can apply the following operations:
# - Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
# - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
# It can be proven that 81 is the highest score one can obtain.

MOD = 10 ** 9 + 7
MX = 10 ** 5 + 1
prime_factors = [0] * MX
for i in range(2, MX): 
    if prime_factors[i] == 0: 
        for j in range(i, MX, i): 
            prime_factors[j] += 1


def maximumScore(nums, k):
    n = len(nums)
    left = [-1] * n
    right = [n] * n
    st = []
    #setting left, right boundaries for current index where it can be max prime score, Using Monotonic Stack
    for i, v in enumerate(nums): 
        while st and prime_factors[nums[st[-1]]] < prime_factors[v]: 
            right[st.pop()] = i
        if st: 
            left[i] = st[-1]
        st.append(i)
    #Greedy Selection of Elements
    ans = 1
    for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda x: -x[1]): 
        tot = (i - l) * (r - i)
        if tot >= k: 
            ans = ans * pow(v, k, MOD) % MOD
            break
        ans = ans * pow(v, tot, MOD) % MOD
        k -= tot
    
    return ans

nums = [8,3,9,3,8]
k = 2
print(maximumScore(nums, k))  # Output: 81
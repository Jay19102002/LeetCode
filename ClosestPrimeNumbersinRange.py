# Example 1:
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.

# Example 2:
# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

def closestPrime(left,right):
    if left > right:
            return [-1,-1]
        
    prime = [True] * (right+1)
    prime[0] = prime[1] = False
    for i in range(2,int(right ** 0.5)+1):
        if prime[i]:
            for j in range(i*i, right+1,i):
                prime[j] = False
    primes = [i for i in range(left,right+1)if prime[i]]
    if len(primes) < 2:
        return [-1,-1]
    
    min_diff,num1,num2 = float('inf'),-1,-1
    for i in range(1,len(primes)):
        diff = primes[i] - primes[i-1]
        if diff < min_diff:
            min_diff = diff
            num1,num2 = primes[i-1],primes[i]
    return [num1,num2]
        

left = 4
right = 6
print(closestPrime(left,right))
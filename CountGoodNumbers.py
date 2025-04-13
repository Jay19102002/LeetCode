# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

MOD = 10**9 + 7

def modExp( base, exp):
    result = 1
    base %= MOD
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return result
    
def countGoodNumbers(n):
    evens = (n + 1) // 2
    odds = n // 2
    evenPart = modExp(5, evens)
    oddPart = modExp(4, odds)
    return (evenPart * oddPart) % MOD
    

n = 4
print(countGoodNumbers(n))  
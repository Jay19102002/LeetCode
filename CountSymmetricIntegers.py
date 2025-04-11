# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

def countSymmetricIntegers(low, high):
    count = 0  # 🍜 Mission count
    for num in range(low, high + 1):
        s = str(num)  # 🔍 Naruto's string transformation no jutsu
        n = len(s)
        if n % 2 != 0:
            continue  # ☠️ Odd-digit numbers are not balanced, skip
        half = n // 2
        left = sum(int(s[i]) for i in range(half))  # ⬅️ Left chakra
        right = sum(int(s[i]) for i in range(half, n))  # ➡️ Right chakra
        if left == right:
            count += 1  # ✅ Symmetry detected, add to mission count
    return count

low = 1
high = 100
print(countSymmetricIntegers(low, high)) 
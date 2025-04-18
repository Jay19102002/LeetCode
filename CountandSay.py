# Input: n = 4

# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

def countAndSay(n):
    if n == 1:
        return "1"
        
    prev = countAndSay(n - 1)
    result = ""
    count = 1
    
    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1
    
    result += str(count) + prev[-1]
    
    return result
    
n = 6
print(countAndSay(n)) 
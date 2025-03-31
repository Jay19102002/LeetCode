# Input: weights = [1,3,5,1], k = 2
# Output: 4
# Explanation: 
# The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
# The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
# Thus, we return their difference 10 - 6 = 4.

def putMarbles(weights, k):
    if k == 1:
            return 0
        
    pair_sum = []
    for i in range(len(weights)-1):
        pair_sum.append(weights[i] + weights[i+1])
    
    pair_sum.sort()
    min = sum(pair_sum[:k-1])
    max = sum(pair_sum[-(k-1):])
    
    return max - min

weights = [1,3,5,1]
k = 2
print(putMarbles(weights, k))  
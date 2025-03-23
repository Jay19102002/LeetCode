# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
# Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
# The four ways to get there in 7 minutes are:
# - 0 ➝ 6
# - 0 ➝ 4 ➝ 6
# - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
# - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
from collections import defaultdict
from heapq import heappop, heappush

def countPaths(n, roads):
    mod = 10**9 + 7
    
    # Adjacency list
    adj = defaultdict(list)
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    pq = [(0, 0)]
    
        # Dijkstra's algorithm
    dist = [float('inf')] * n
    dist[0] = 0

    # Count of shortest paths to each node
    count = [0] * n
    count[0] = 1
    
    while pq:
        d, node = heappop(pq)
        
        if d > dist[node]:
            continue
        
        for neighbor, weight in adj[node]:
            if d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                count[neighbor] = count[node]
                
                heappush(pq, (dist[neighbor], neighbor))
                
            elif d + weight == dist[neighbor]:
                count[neighbor] += count[node]
                count[neighbor] %= mod
                
    return count[n - 1] % mod

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n, roads))
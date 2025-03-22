# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.
from collections import defaultdict

def countCompleteComponents(n, edges):
    visit = set()
    graph = defaultdict(list)
    count = 0
    
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    def dfs(node,component):
        component.add(node)
        visit.add(node)
        for neighbor in graph[node]:
            if neighbor not in visit:
                dfs(neighbor,component)
        
    for i in range(n):
        if i not in visit:
            component = set()
            dfs(i,component)
            if all(len(graph[node]) == len(component) -1 for node in component):
                count += 1
    return count

n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
print(countCompleteComponents(n, edges))
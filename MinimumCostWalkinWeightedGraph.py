def minimumCost(n, edges, query):
    parent = [i for i in range(n)]
    def root(u):
        if u == parent[u]:
            return u
        parent[u] = root(parent[u])
        return parent[u]
    
    size = [1]*n
    AND = [(1 << 31)-1]*n
    def union_by_size(u,v,w):
        u = root(u)
        v = root(v)
        if u == v:
            AND[u]&=w
            return
        if size[u] < size[v]:
            u,v = v,u
        
        size[u] += size[v]
        parent[v] = u
        AND[u] = AND[u]&AND[v]&w
    for u,v,w in edges:
        union_by_size(u,v,w)
    ans = []
    for u,v in query:
        if u==v:
            ans.append(0)
        elif root(u) == root(v):
            ans.append(AND[root(u)])
        else:
            ans.append(-1)
    return ans

n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]
print(minimumCost(n, edges, query))
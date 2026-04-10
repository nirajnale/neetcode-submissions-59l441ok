class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            pu, pv = find(u), find(v)

            if pu == pv:
                return [u, v]

            parent[pu] = pv
            
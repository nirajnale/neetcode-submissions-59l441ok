from collections import defaultdict

class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)

        dfs(0)

        return len(visited) == n
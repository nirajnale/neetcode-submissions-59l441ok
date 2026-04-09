from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # Queue for courses with no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []
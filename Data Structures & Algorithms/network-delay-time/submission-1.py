import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)

        # Build graph
        for u, v, w in times:
            adj[u].append((v, w))

        heap = [(0, k)]  # (time, node)
        visited = set()
        maxTime = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            maxTime = max(maxTime, time)

            for nei, w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + w, nei))

        return maxTime if len(visited) == n else -1
        
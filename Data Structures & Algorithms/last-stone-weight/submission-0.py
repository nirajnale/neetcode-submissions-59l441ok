import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use negative values to simulate a max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if y != x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0

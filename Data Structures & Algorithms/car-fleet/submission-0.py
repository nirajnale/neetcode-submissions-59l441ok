from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)  # sort by position descending

        stack = []

        for p, s in pairs:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)
            # else: joins fleet (do nothing)

        return len(stack)
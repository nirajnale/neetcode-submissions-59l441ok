from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, subset):
            if index == len(nums):
                res.append(subset[:])
                return

            # Exclude nums[index]
            backtrack(index + 1, subset)

            # Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

        backtrack(0, [])
        return res

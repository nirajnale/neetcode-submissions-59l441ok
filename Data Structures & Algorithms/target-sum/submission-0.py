class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)

        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        P = (target + total) // 2

        dp = [0] * (P + 1)
        dp[0] = 1

        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[P]
class Solution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    if dp[i + len(word)]:
                        dp[i] = True
                        break

        return dp[0]
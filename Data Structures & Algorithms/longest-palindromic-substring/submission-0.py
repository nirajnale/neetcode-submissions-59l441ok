class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # Odd length
            temp = expand(i, i)
            if len(temp) > resLen:
                res = temp
                resLen = len(temp)

            # Even length
            temp = expand(i, i+1)
            if len(temp) > resLen:
                res = temp
                resLen = len(temp)

        return res
        
class Solution:
    def partitionLabels(self, s: str):
        last = {c: i for i, c in enumerate(s)}
        
        res = []
        start = end = 0

        for i in range(len(s)):
            end = max(end, last[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
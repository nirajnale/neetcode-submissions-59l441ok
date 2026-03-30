class Solution:
    def encode(self, strs):
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1  # move past '#'

            res.append(s[j:j + length])
            i = j + length

        return res

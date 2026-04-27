class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # to simulate 32-bit integer
        max_int = 0x7FFFFFFF
        
        while b != 0:
            # XOR gives sum without carry
            sum_ = (a ^ b) & mask
            # AND + shift gives the carry
            carry = ((a & b) << 1) & mask
            
            a, b = sum_, carry
        
        # if a <= max_int, it's positive
        # else convert to negative using two's complement
        return a if a <= max_int else ~(a ^ mask)
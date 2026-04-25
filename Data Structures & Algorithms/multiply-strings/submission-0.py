class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # multiply each digit
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = int(num1[i]) * int(num2[j])
                summ = mul + result[i + j + 1]
                
                result[i + j + 1] = summ % 10
                result[i + j] += summ // 10
        
        # convert to string
        res_str = ''.join(map(str, result))
        # remove leading zeros
        return res_str.lstrip('0')
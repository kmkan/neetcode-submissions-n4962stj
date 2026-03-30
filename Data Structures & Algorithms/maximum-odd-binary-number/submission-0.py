class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        bits = {'1': 0, '0': 0}

        for bit in s:
            bits[str(bit)] += 1
        
        ans = []

        while bits['1'] > 1:
            ans.append('1')
            bits['1'] -= 1
        
        while bits['0'] > 0:
            ans.append('0')
            bits['0'] -= 1
        
        ans.append('1')

        return ''.join(ans)
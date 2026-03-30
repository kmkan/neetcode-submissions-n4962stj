class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 31

        while n > 0:
            ans = ans + (n & 1) * 2 ** power
            print(ans)
            power -= 1
            n >>= 1
        
        return ans


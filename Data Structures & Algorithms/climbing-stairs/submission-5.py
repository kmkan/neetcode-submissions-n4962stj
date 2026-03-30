class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        step0 = 1
        step1 = 1
        for i in range(2, n):
            result = step0 + step1
            step0 = step1
            step1 = result
        
        return step0 + step1
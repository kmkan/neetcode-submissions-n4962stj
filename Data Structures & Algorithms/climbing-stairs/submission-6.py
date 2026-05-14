class Solution:
    def climb(self, n, dp):
        if n <= 1:
            return 1
        
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.climb(n - 1, dp) + self.climb(n - 2, dp)

        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.climb(n, dp)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1
        for i in range(1, n):
            dp[0][i] = 1
        
        for row in range(1, m):
            for col in range(0, n):
                up = dp[row - 1][col]
                left = 0
                if col > 0:
                    left = dp[row][col - 1]
                dp[row][col] = up + left
        
        return dp[-1][-1]

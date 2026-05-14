class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf') for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                    continue
                left = float('inf')
                if j > 0:
                    left = dp[j - 1]
                dp[j] = grid[i][j] + min(dp[j], left)
            print(dp)
        return dp[n - 1]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = float('inf')
                left = float('inf')

                if i > 0:
                    up = dp[i - 1][j]
                if j > 0:
                    left = dp[i][j - 1]
                    print(i, j, left + grid[i][j])

                dp[i][j] = grid[i][j] + min(up, left)
        
                print(dp)
        return dp[m - 1][n - 1]
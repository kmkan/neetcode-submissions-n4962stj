class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def path_helper(i, j, dp):
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i < 0 or j < 0:
                return float('inf')

            if dp[i][j] != -1:
                return dp[i][j]
            
            up = path_helper(i - 1, j, dp)
            left = path_helper(i, j - 1, dp)

            dp[i][j] = grid[i][j] + min(up, left)
            return dp[i][j]

        return path_helper(m - 1, n - 1, dp)
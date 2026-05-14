class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def path_helper(row, col, dp):
            if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
                return 0
            
            if row == 0 and col == 0:
                return 1
            
            if dp[row][col] != -1:
                return dp[row][col]

            left = path_helper(row, col - 1, dp)
            up = path_helper(row - 1, col, dp)
            dp[row][col] = left + up
            
            return left + up
        
        return path_helper(m - 1, n - 1, dp)
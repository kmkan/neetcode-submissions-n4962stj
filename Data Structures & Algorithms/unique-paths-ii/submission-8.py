class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
                
        return dp[-1]

        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             continue

        #         if i == 0 and j == 0:
        #             dp[i][j] = 1
        #             continue
                
        #         up = 0
        #         left = 0

        #         if i > 0:
        #             up = dp[i - 1][j]
        #         if j > 0:
        #             left = dp[i][j - 1]
                
        #         dp[i][j] = up + left
        
        # return dp[m - 1][n - 1]


        # def path_helper(row, col, dp):
        #     if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
        #         return 0
            
        #     if row == 0 and col == 0:
        #         return 1
            
        #     if dp[row][col] != -1:
        #         return dp[row][col]

        #     left = path_helper(row, col - 1, dp)
        #     up = path_helper(row - 1, col, dp)
        #     dp[row][col] = left + up

        #     return left + up
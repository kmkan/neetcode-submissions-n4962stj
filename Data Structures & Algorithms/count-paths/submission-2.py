class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        print(dp)
        def path_helper(m, n, dp):
            if m == 1 and n == 1:
                return 1

            if dp[m - 1][n - 1] != -1:
                return dp[m - 1][n - 1]
            
            up = 0
            left = 0

            if m > 1:
                up = path_helper(m - 1, n, dp)
            
            if n > 1:
                left = path_helper(m, n - 1, dp)
            
            dp[m - 1][n - 1] = up + left
            return dp[m - 1][n - 1]
        
        return path_helper(m, n, dp)

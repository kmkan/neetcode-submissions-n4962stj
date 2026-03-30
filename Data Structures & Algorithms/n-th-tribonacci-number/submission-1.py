class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dfs(m):
            if m == 0:
                return 0
            elif m == 1:
                return 1
            elif m == 2:
                return 1
            
            if m in memo:
                return memo[m]
            
            memo[m] = dfs(m - 1) + dfs(m - 2) + dfs(m - 3)
            return memo[m]
        
        return dfs(n)
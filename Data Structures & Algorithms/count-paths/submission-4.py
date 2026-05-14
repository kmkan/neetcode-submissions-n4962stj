class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for i in range(1, m):
            for j in range(0, n):
                up = prev[j]
                left = 0
                if j > 0:
                    left = prev[j - 1]
                prev[j] = up + left
    
        
        return prev[-1]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def climb(m):
            if m >= len(cost):
                return 0
            
            if m in memo:
                return memo[m]
            
            memo[m] = cost[m] + min(climb(m + 1), climb(m + 2))
            return memo[m]
        
        climb(0)
        return min(memo[0], memo[1])


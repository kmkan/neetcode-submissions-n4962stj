class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def climb(m):
            if m >= len(cost):
                return 0
            elif m == len(cost) - 1:
                return cost[m]
            
            if m in memo:
                return memo[m]
            
            memo[m] = cost[m] + min(climb(m + 1), climb(m + 2))
            return memo[m]
        
        climb_0 = climb(0)
        climb_1 = climb(1)
        return min(climb_0, climb_1)


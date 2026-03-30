class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step0 = cost[0]
        step1 = cost[1]

        for i in range(2, len(cost)):
            step0, step1 = step1, cost[i] + min(step0, step1)
        
        return min(step0, step1)
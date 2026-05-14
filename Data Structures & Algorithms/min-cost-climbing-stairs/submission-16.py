class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            step_1 = cost[i] + dp[i - 1]
            step_2 = cost[i] + dp[i - 2]
            dp[i] = min(step_1, step_2)
        
        return min(dp[-1], dp[-2])
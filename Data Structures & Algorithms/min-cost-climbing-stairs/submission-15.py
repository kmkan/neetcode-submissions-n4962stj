class Solution:
    def climb(self, idx, cost, dp):
        if idx <= 1:
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        dp[idx] = min(self.climb(idx - 1, cost, dp) + cost[idx - 1], self.climb(idx - 2, cost, dp) + cost[idx - 2])
        return dp[idx]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        return self.climb(len(cost), cost, dp)
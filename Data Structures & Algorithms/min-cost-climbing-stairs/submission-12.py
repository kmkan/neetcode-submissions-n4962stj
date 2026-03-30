class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step0 = 0
        step1 = 0

        for c in cost:
            step0, step1 = step1, c + min(step0, step1)
        
        return min(step0, step1)
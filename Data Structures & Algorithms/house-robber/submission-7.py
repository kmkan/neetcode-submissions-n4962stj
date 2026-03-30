class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(m):
            if m >= len(nums):
                return 0
            
            if m in memo:
                return memo[m]
            
            memo[m] = max(nums[m] + dp(m + 2), dp(m + 1))
            return memo[m]
        
        return dp(0)

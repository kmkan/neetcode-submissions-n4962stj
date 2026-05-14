class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def rob_helper(idx, dp):
            if idx >= len(nums):
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            dp[idx] = max(nums[idx] + rob_helper(idx + 2, dp), rob_helper(idx + 1, dp))
            return dp[idx]
        
        return rob_helper(0, dp)

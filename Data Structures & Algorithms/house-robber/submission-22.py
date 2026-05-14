class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            rob = dp[i - 1]
            if i > 1:
                no_rob = nums[i] + dp[i - 2]
            else:
                no_rob = nums[i]
            
            dp[i] = max(rob, no_rob)
        
        return dp[-1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def rob_helper(idx, dp):
            if idx == 0:
                return nums[0]
            if idx == 1:
                return max(nums[0], nums[1])
            if dp[idx] != -1:
                return dp[idx]
            rob = nums[idx] + rob_helper(idx - 2, dp)
            no_rob = rob_helper(idx - 1, dp)
            dp[idx] = max(rob, no_rob)
            return dp[idx]
        
        return rob_helper(len(nums) - 1, dp)
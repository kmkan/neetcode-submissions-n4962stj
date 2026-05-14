class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1] * len(nums)
        def rob_helper(min_idx, cur_idx, dp):
            if cur_idx == min_idx:
                return nums[cur_idx]
            if cur_idx < min_idx:
                return 0
            
            if dp[cur_idx] != -1:
                return dp[cur_idx]
            
            rob = nums[cur_idx] + rob_helper(min_idx, cur_idx - 2, dp)
            no_rob = rob_helper(min_idx, cur_idx - 1, dp)
            dp[cur_idx] = max(rob, no_rob)
            return dp[cur_idx]
        
        first_house = rob_helper(0, len(nums) - 2, dp)
        dp = [-1] * len(nums)
        not_first_house = rob_helper(1, len(nums) - 1, dp)
        return max(first_house, not_first_house)
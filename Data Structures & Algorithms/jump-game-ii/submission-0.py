class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(idx):
            if idx >= len(nums) - 1:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            memo[idx] = len(nums)
            for i in range(1, nums[idx] + 1):
                memo[idx] = min(memo[idx], 1 + dp(idx + i))
            
            return memo[idx]
        
        return dp(0)
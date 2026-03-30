class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(m):
            if m >= len(nums):
                return 0
            
            if m in memo:
                return memo[m]
            
            memo[m] = nums[m] + max(dfs(m + 2), dfs(m + 3))
            return memo[m]
        
        dfs(0)
        dfs(1)
        
        if len(nums) >= 2:
            return max(memo[0], memo[1])
        else:
            return memo[0]
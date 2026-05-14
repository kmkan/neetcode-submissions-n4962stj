class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            cur_i = max(prev, prev2 + nums[i])
            
            prev2, prev = prev, cur_i
        
        return prev
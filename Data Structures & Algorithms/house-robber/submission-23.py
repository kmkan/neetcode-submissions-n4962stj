class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                cur_i = max(prev, nums[1])
            else:
                cur_i = max(prev2 + nums[i], prev)
            
            prev2, prev = prev, cur_i
        
        return prev
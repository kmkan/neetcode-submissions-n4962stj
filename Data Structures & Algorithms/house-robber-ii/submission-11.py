class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            prev2 = 0
            prev = nums[0]

            for i in range(1, len(nums)):
                cur_i = max(prev, nums[i] + prev2)
                prev2, prev = prev, cur_i
            
            return prev
        
        if len(nums) == 1:
            return nums[0]
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:len(nums) - 1]))
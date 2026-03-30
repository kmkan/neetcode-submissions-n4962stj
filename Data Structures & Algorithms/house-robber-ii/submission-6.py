class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def house_robber(houses: List[int]) -> int:
            step0 = 0
            step1 = 0

            for h in houses:
                step0, step1 = step1, max(step1, step0 + h)
            
            return step1
        
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))
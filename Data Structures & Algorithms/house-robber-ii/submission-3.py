class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        step0_0 = 0
        step1_0 = 0

        step0_1 = 0
        step1_1 = 0

        for i in range(len(nums)):
            if i < len(nums) - 1:
                step0_0, step1_0 = step1_0, max(step1_0, nums[i] + step0_0)
            
            if i > 0:
                step0_1, step1_1 = step1_1, max(step1_1, nums[i] + step0_1)
            
            print(step0_0, step0_1)

        return max(step1_0, step1_1)
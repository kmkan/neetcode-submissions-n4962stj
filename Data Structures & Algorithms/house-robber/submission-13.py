class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]

        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        # return max(dp[-1], dp[-2])
        step0 = 0
        step1 = 0

        for n in nums:
            step0, step1 = step1, max(step1, step0 + n)
        
        return max(step0, step1)
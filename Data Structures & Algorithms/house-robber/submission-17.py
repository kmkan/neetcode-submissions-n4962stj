class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        prev2 = dp[0]
        prev = dp[1]
        for i in range(2, len(nums)):
            cur_i = max(prev, nums[i] + prev2)
            prev2, prev = prev, cur_i
        return prev

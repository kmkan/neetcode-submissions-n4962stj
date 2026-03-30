class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums) + i):
                if cur_sum < 0:
                    cur_sum = 0
                cur_sum += nums[(i + j) % len(nums)]
                max_sum = max(cur_sum, max_sum)
        
        return max_sum
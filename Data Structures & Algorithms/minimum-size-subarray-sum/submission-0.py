class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        min_size = len(nums)
        left = 0
        right = 0
        cur_sum = 0
        while right < len(nums):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_size = min(min_size, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_size



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left = 0
        right = 0
        cur_sum = 0
        min_size = len(nums)

        while right < len(nums):
            if cur_sum < target:
                cur_sum += nums[right]
                right += 1
            else:
                min_size = min(min_size, right - left)
                cur_sum -= nums[left]
                left += 1
            print(cur_sum)
        
        while left < len(nums) and cur_sum >= target:
            min_size = min(min_size, right - left)
            cur_sum -= nums[left]
            left += 1
        
        return min_size
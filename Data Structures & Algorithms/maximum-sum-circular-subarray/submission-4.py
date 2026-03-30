class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        cur_max_sum = 0
        cur_min_sum = 0
        total = 0

        for n in nums:
            total += n
            if cur_max_sum < 0:
                cur_max_sum = 0
            if cur_min_sum > 0:
                cur_min_sum = 0
            
            cur_max_sum += n
            cur_min_sum += n
            max_sum = max(cur_max_sum, max_sum)
            print(cur_min_sum, cur_max_sum, max_sum)
            min_sum = min(cur_min_sum, min_sum)
        
        print(total, min_sum, max_sum)
        if min_sum == total:
            return max_sum
        return max(total - min_sum, max_sum)
        
        


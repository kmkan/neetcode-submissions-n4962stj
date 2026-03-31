class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_nums = {}

        for i, n in enumerate(nums):
            k = target - n
            if k in pos_nums:
                return [pos_nums[k], i]
            
            pos_nums[n] = i
        
        return None
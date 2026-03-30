class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_num = {}

        for i in range(len(nums)):
            k = target - nums[i]

            if k in pos_num:
                return [pos_num[k], i]
            
            pos_num[nums[i]] = i
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_nums = {}

        for i in range(len(nums)):
            k = target - nums[i]
            if k in pos_nums:
                return [pos_nums[k], i]
            pos_nums[nums[i]] = i
        
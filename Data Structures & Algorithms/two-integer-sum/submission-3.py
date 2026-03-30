class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}

        for i in range(len(nums)):
            k = target - nums[i]
            if k in num_pos:
                return [num_pos[k], i]
            num_pos[nums[i]] = i
            
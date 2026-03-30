class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_pos = {}
        nums = numbers
        for i in range(len(nums)):
            if target - nums[i] in nums_pos:
                return [nums_pos[target - nums[i]] + 1, i + 1]
            else:
                nums_pos[nums[i]] = i
        
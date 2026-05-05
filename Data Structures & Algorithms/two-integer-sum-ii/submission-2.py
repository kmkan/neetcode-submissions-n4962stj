class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pos_nums = {}

        for i, num in enumerate(numbers):
            if target - num in pos_nums:
                return [pos_nums[target - num] + 1, i + 1]
            else:
                pos_nums[num] = i
        


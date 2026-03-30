import random
class Solution:
    def quickSort(self, nums: List[int], begin: int, end: int) -> List[int]:
        if begin >= end:
            return nums
        
        random_idx = random.randint(begin, end)
        nums[end], nums[random_idx] = nums[random_idx], nums[end]

        i = begin
        j = begin

        while j < end:
            if nums[j] <= nums[end]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        
        nums[j], nums[i] = nums[i], nums[j]

        self.quickSort(nums, begin, i - 1)
        self.quickSort(nums, i + 1, end)
        
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)
        
import random
class Solution:
    def quickSort(self, arr: List[int], begin: int, end: int) -> List[int]:
        if begin >= end:
            return arr
        
        rand_idx = random.randint(begin, end)
        arr[end], arr[rand_idx] = arr[rand_idx], arr[end]

        pivot_index = end
        i = begin
        j = begin

        while j < pivot_index:
            if arr[j] <= arr[pivot_index]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1
        arr[i], arr[j] = arr[j], arr[i]
        self.quickSort(arr, begin, i - 1)
        self.quickSort(arr, i + 1, end)
        return arr
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums) - 1)
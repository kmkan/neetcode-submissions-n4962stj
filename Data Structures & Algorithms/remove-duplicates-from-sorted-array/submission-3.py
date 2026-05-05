class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[cur]:
                cur += 1
                k += 1
                nums[cur] = nums[i]
        
        return k + 1
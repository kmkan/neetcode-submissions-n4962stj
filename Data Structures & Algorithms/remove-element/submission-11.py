class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_pos = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[cur_pos] = nums[i]
                cur_pos += 1
        
        return cur_pos
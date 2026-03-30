class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != val:
                left += 1
            if nums[right] == val:
                right -= 1
        
        # print(left)
        # for num in nums:
        #     if num == val:
        #         break
        #     k += 1
        # return k
        if left >= len(nums) or nums[left] != val:
            return left + 1
        return left
        
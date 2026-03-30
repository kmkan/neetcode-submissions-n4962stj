class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        k = 0
        while left < right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != val:
                left += 1
            if nums[right] == val:
                right -= 1
        
        for num in nums:
            print(num, val)
            if num == val:
                break
            k += 1
        return k
        
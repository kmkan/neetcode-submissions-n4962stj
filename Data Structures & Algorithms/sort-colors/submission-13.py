class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        cur = 0

        while cur <= two:
            if nums[cur] == 0:
                nums[cur], nums[zero] = nums[zero], nums[cur]
                zero += 1
            if nums[cur] == 2:
                nums[cur], nums[two] = nums[two], nums[cur]
                two -= 1
            else:
                cur += 1
        
        
        
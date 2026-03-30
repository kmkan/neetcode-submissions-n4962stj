class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if furthest == i:
                return False
        
        return True
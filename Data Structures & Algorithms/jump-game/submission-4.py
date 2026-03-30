class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0

        for i in range(len(nums) - 1):
            distance = max(distance, i + nums[i])
            if distance == i:
                return False
        
        return True
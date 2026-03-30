class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def backtrack(idx):
            if idx == len(nums) - 1:
                return True
            elif idx >= len(nums):
                return False
            
            possible = False
            for i in range(1, nums[idx] + 1):
                possible = possible or backtrack(idx + i)
            
            return possible
        
        return backtrack(0)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_pos = {}

        for i in range(len(nums)):
            if nums[i] in num_pos and i - num_pos[nums[i]] <= k:
                return True
            else:
                num_pos[nums[i]] = i
        
        return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos_nums = {}

        for i, n in enumerate(nums):
            if n in pos_nums and abs(i - pos_nums[n]) <= k:
                return True
            pos_nums[n] = i

        return False
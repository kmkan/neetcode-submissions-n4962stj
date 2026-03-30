class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cur_nums = set()
        for num in nums:
            if num in cur_nums:
                return True
            cur_nums.add(num)
        return False
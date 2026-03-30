from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set()
        lower = min(nums)
        upper = max(nums)
        for num in nums:
            nums_set.add(num)
        
        cur_seq_len = 0
        max_seq_len = 0
        for i in range(lower, upper + 1):
            if i in nums_set:
                cur_seq_len += 1
            else:
                max_seq_len = max(max_seq_len, cur_seq_len)
                cur_seq_len = 0
                i -= 1
        return max(max_seq_len, cur_seq_len)
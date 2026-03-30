from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)

        max_seq_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_seq_len = 1
                i = num
                while i + 1 in nums_set:
                    cur_seq_len += 1
                    i += 1
                max_seq_len = max(max_seq_len, cur_seq_len)
        
        return max_seq_len


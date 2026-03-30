class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        set_nums = set(nums)
        for num in nums:
            if num - 1 not in set_nums:
                cur_seq = 0
                while num in set_nums:
                    cur_seq += 1
                    num += 1
                longest_seq = max(longest_seq, cur_seq)
        
        return longest_seq
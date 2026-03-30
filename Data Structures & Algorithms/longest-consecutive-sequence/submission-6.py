class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        max_seq = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                cur_seq = 1
                while num + 1 in set_nums:
                    cur_seq += 1
                    num += 1
                max_seq = max(max_seq, cur_seq)
        
        return max_seq
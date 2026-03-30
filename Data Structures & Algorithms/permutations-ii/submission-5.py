class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(cur_nums, used):
            if len(cur_nums) == len(nums):
                ans.append(cur_nums.copy())
                return
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                cur_nums.append(nums[i])
                backtrack(cur_nums, used)
                used[i] = False
                cur_nums.pop()
        
        backtrack([], [False] * len(nums))
        return ans
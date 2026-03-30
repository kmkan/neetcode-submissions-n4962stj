class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(cur_nums, used):
            if len(cur_nums) == len(nums) and tuple(cur_nums) not in ans:
                ans.append(tuple(cur_nums))
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur_nums.append(nums[i])
                backtrack(cur_nums, used)
                used[i] = False
                cur_nums.pop()
        
        backtrack([], [False] * len(nums))
        return ans
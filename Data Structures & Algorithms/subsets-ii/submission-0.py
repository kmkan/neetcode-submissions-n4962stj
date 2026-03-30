class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        def backtrack(idx, cur_nums):
            ans.append(cur_nums.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                cur_nums.append(nums[i])
                backtrack(i + 1, cur_nums)
                cur_nums.pop()
        
        backtrack(0, [])
        return ans
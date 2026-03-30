class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(cur_nums):
            if len(cur_nums) == len(nums):
                ans.append(cur_nums.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in cur_nums:
                    continue
                cur_nums.append(nums[i])
                backtrack(cur_nums)
                cur_nums.pop()
        
        backtrack([])
        return ans
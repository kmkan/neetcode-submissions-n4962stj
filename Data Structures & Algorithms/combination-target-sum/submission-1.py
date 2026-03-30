class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(idx, total_sum, cur_nums):
            if total_sum == target:
                ans.append(cur_nums.copy())
                return []
            elif total_sum > target:
                return []
            
            for i in range(idx, len(nums)):
                cur_nums.append(nums[i])
                backtrack(i, total_sum + nums[i], cur_nums)
                cur_nums.pop()
        
        backtrack(0, 0, [])
        return ans
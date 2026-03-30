class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []


        def backtrack(idx, cur_nums):
            total = sum(cur_nums)

            if total == target:
                ans.append(cur_nums.copy())
                return []
            elif total > target:
                return []
            else:
                for i in range(idx, len(nums)):
                    cur_nums.append(nums[i])
                    backtrack(i, cur_nums)
                    cur_nums.pop()
        
        backtrack(0, [])
        return ans
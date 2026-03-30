class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, cur_nums):
            cur_nums = cur_nums.copy()
            
            ans.append(cur_nums)

            for i in range(idx, len(nums)):
                cur_nums.append(nums[i])
                
                backtrack(i + 1, cur_nums)

                cur_nums.pop()
        backtrack(0, [])
        return ans
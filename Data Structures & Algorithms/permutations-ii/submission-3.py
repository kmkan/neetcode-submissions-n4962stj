class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(cur_nums, cur_idx):
            if len(cur_nums) == len(nums) and tuple(cur_nums) not in ans:
                ans.append(tuple(cur_nums))
            
            for i in range(0, len(nums)):
                if i in cur_idx:
                    continue
                cur_idx.add(i)
                cur_nums.append(nums[i])
                backtrack(cur_nums, cur_idx)
                cur_idx.remove(i)
                cur_nums.pop()
        
        backtrack([], set())
        return ans
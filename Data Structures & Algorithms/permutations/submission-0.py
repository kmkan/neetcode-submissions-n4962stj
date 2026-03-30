class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, cur_nums):
            if len(cur_nums) == len(nums):
                ans.append(cur_nums.copy())
                return
            
            for i in range(idx, len(nums) + idx):
                if nums[i % len(nums)] in cur_nums:
                    continue
                cur_nums.append(nums[i % len(nums)])
                backtrack(i + 1, cur_nums)
                cur_nums.pop()
        
        backtrack(0, [])
        return ans
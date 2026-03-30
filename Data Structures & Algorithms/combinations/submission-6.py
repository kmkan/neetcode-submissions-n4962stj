class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(idx, cur_nums):
            if len(cur_nums) == k:
                ans.append(cur_nums.copy())
                return
            

            need = k - len(cur_nums)
            upper_bound = n - need + 1
            for i in range(idx, upper_bound + 1):
                cur_nums.append(i)
                backtrack(i + 1, cur_nums)
                cur_nums.pop()
        
        backtrack(1, [])
        return ans
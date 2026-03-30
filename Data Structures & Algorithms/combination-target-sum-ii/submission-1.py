class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def backtrack(idx, total_sum, cur_nums):
            if total_sum == target:
                ans.add(tuple(sorted(cur_nums)))
                return []
            elif total_sum > target:
                return []
            
            for i in range(idx, len(candidates)):
                cur_nums.append(candidates[i])
                backtrack(i + 1, total_sum + candidates[i], cur_nums)
                cur_nums.pop()
        
        backtrack(0, 0, [])
        return [list(l) for l in ans]
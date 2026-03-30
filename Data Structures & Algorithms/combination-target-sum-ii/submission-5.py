class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(idx, total, cur_nums):
            if total == target:
                ans.append(cur_nums.copy())
                return []
            elif total > target:
                return []
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] + total > target:
                    break
                cur_nums.append(candidates[i])
                backtrack(i + 1, total + candidates[i], cur_nums)
                cur_nums.pop()
        
        backtrack(0, 0, [])
        return ans
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        def backtrack(idx, xor_total):
            ans.append(xor_total)
            for i in range(idx, len(nums)):
                backtrack(i + 1, xor_total ^ nums[i])
        
        backtrack(0, 0)
        return sum(ans)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []

        def backtrack(idx, xor_val):
            ans.append(xor_val)
            for i in range(idx, len(nums)):
                backtrack(i + 1, xor_val ^ nums[i])
        
        backtrack(0, 0)
        return sum(ans)
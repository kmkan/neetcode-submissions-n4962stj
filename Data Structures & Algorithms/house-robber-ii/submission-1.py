class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        last_removed = nums[:len(nums) - 1]

        memo_zero = {}
        memo_one = {}
        
        def dfs(m: int, arr: List[int], memo: dict):
            if m >= len(arr):
                return 0
            
            if m in memo:
                return memo[m]
            
            memo[m] = max(arr[m] + dfs(m + 2, arr, memo), dfs(m + 1, arr, memo))

            return memo[m]

        dfs(0, last_removed, memo_zero)
        dfs(1, nums, memo_one)
        return max(memo_zero[0], memo_one[1])

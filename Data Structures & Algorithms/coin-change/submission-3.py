class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(total):
            if total == amount:
                return 0
            elif total > amount:
                return -1
            

            if total in memo:
                return memo[total]
            
            counts = []
            for c in coins:
                counts.append(dp(total + c))
            
            counts = [c for c in counts if c != -1]
            if counts:
                memo[total] = 1 + min(counts)
            else:
                memo[total] = -1
            return memo[total]
        
        return dp(0)

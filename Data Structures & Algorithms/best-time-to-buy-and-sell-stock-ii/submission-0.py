class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        cur_price = prices[0]

        for p in prices:
            if p < cur_price:
                cur_price = p
            
            if p - cur_price > 0:
                total_profit += p - cur_price
                cur_price = p
        
        return total_profit
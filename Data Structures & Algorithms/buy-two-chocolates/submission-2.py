class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_price = float('inf')
        min_choc = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, min_choc + prices[i])
            if prices[i] < min_choc:
                min_choc = prices[i]
        
        if min_price > money:
            return money
        
        return money - min_price
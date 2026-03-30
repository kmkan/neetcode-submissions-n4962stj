class Solution:
    def ship(self, weights: List[int], w: int) -> int:
        days = 0
        cur_weight = 0

        for wei in weights:
            if wei + cur_weight > w:
                days += 1
                cur_weight = 0
            cur_weight += wei
        

        return days + 1
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)

        while min_weight <= max_weight:
            mid = min_weight + (max_weight - min_weight) // 2
            d = self.ship(weights, mid)
            print(d, mid)
            if d <= days:
                max_weight = mid - 1
            else:
                min_weight = mid + 1
        
        return min_weight
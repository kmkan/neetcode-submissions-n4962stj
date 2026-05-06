class Solution:
    def days(self, weights, shipWeight):
        total_days = 0
        cur_weight = 0

        for weight in weights:
            if cur_weight + weight > shipWeight:
                total_days += 1
                cur_weight = 0
            cur_weight += weight
        
        return total_days + 1
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)

        while min_weight <= max_weight:
            weight = min_weight + (max_weight - min_weight) // 2
            total_days = self.days(weights, weight)
            if total_days <= days:
                max_weight = weight - 1
            else:
                min_weight = weight + 1
        
        return min_weight
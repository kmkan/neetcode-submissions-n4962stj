class Solution:
    def eat(self, piles: List[int], k: int) -> int:
        total_hours = 0

        for p in piles:
            if p % k != 0:
                total_hours = total_hours + p // k + 1
            else:
                total_hours = total_hours + p // k
        
        return total_hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        best_speed = max_speed
        while min_speed <= max_speed:
            speed = min_speed + (max_speed - min_speed) // 2
            if self.eat(piles, speed) <= h:
                best_speed = speed
                max_speed = speed - 1
            else:
                min_speed = speed + 1
        
        return best_speed
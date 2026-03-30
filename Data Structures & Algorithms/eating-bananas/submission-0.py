class Solution:
    def eat(self, piles: List[int], k: int) -> int:
        total_h = 0
        for p in piles:
            total_h += math.ceil(p / k)
        return total_h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        possible_rate = 0
        while min_rate <= max_rate:
            mid = min_rate + (max_rate - min_rate) // 2
            print(mid)
            if self.eat(piles, mid) > h:
                min_rate = mid + 1
            else:
                possible_rate = mid
                max_rate = mid - 1
        
        return possible_rate



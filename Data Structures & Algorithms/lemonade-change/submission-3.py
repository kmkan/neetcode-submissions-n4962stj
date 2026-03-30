import heapq
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            print("Before: ", b, (fives, tens))
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
            b -= 5
            if b == 0:
                continue
            elif b == 5 and fives >= 1:
                fives -= 1
            elif b == 15 and tens >= 1 and fives >= 1:
                tens -= 1
                fives -= 1
            elif b == 15 and fives >= 3:
                fives -= 3
            else:
                return False
        return True
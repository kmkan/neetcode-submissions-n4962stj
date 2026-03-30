import heapq
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur_change = {5: 0, 10: 0, 20: 0}

        for b in bills:
            print("Before:", b, cur_change)
            cur_change[b] += 1
            b -= 5
            if b == 0:
                print("After: ", b, cur_change)
                continue
            elif b == 5 and cur_change[5] >= 1:
                cur_change[5] -= 1
            elif b == 10 and cur_change[10] >= 1:
                cur_change[10] -= 1
            elif b == 10 and cur_change[5] >= 2:
                cur_change[5] -= 2
            elif b == 15 and cur_change[10] >= 1 and cur_change[5] >= 1:
                cur_change[10] -= 1
                cur_change[5] -= 1
            elif b == 15 and cur_change[5] >= 3:
                cur_change[5] -= 3
            else:
                return False
            print("After: ", b, cur_change)
        return True
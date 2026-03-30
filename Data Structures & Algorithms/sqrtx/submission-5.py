class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = left + (right - left) // 2

            if mid != 0:
                if mid == x // mid:
                    return mid
                elif mid < x // mid:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                break
        
        return right
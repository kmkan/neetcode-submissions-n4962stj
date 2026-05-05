class Solution:
    def isPalin(self, s: str, left: int, right: int) -> bool:
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalin(s, left + 1, right) or self.isPalin(s, left, right - 1)
            else:
                left += 1
                right -= 1
        
        return True
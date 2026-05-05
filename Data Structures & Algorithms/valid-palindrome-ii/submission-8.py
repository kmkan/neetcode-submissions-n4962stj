class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[:left] + s[left + 1:]) or self.isPalindrome(s[:right] + s[right + 1:])
            else:
                left += 1
                right -= 1














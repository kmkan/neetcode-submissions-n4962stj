class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        def palindrome(left: int, right: int, s: str) -> int:
            pal = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pal += 1
                left -= 1
                right += 1
            
            return pal

        for i in range(len(s)):
            palindromes += palindrome(i, i, s)
            palindromes += palindrome(i, i + 1, s)
            
        return palindromes
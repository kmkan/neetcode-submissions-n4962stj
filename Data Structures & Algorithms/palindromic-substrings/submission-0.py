class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = []

        def palindrome(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes.append(s[left:right + 1])
                left -= 1
                right += 1
            
            s = s[left + 1:right]
            if s:
                return s

        for i in range(len(s)):
            palindrome(i, i, s)
            palindrome(i, i + 1, s)
            
        print(palindromes)
        return len(palindromes)
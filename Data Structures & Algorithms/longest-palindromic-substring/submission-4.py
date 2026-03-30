class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def palindrome(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        
        for i in range(len(s)):
            odd_pal = palindrome(i, i, s)
            even_pal = palindrome(i, i + 1, s)
            cur_longest = even_pal if len(even_pal) > len(odd_pal) else odd_pal

            longest = longest if len(longest) > len(cur_longest) else cur_longest
        return longest
        

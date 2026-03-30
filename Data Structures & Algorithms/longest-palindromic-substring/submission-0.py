class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_s = s[i:j + 1]
                if cur_s == cur_s[::-1]:
                    if len(cur_s) > len(longest):
                        longest = cur_s
        
        return longest
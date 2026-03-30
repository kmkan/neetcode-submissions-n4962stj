class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}

        for char in s:
            chars_s[char] = chars_s.get(char, 0) + 1
        for char in t:
            if char not in chars_s:
                return False
            chars_s[char] -= 1
            if chars_s[char] == 0:
                del chars_s[char]
        
        return len(chars_s) == 0
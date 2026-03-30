class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}

        for c in s:
            chars_s[c] = chars_s.get(c, 0) + 1
        
        for c in t:
            if c not in chars_s:
                return False
            else:
                chars_s[c] -= 1
                if chars_s[c] == 0:
                    del chars_s[c]
        
        return len(chars_s) == 0
        
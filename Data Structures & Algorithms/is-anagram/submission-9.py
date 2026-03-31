class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}

        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        
        for c in t:
            if c not in dict_s:
                return False
            dict_s[c] -= 1
            if dict_s[c] == 0:
                del dict_s[c]
        
        return True
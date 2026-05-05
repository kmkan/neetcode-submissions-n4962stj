class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        
        for c in t:
            if c not in count_s:
                return False
            count_s[c] -= 1
            if count_s[c] == 0:
                del count_s[c]

        return len(count_s) == 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        for c in count_t:
            if c not in count_s or count_s[c] != count_t[c]:
                return False
        
        return len(count_s) == len(count_t)
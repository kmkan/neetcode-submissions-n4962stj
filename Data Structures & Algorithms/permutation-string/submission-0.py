class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        chars_s1 = {}

        for c in s1:
            chars_s1[c] = chars_s1.get(c, 0) + 1
        

        left = 0
        right = 0
        chars_s2 = {}

        while right < len(s2):
            chars_s2[s2[right]] = chars_s2.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                chars_s2[s2[left]] -= 1
                if chars_s2[s2[left]] == 0:
                    del chars_s2[s2[left]]
                left += 1
            
            if len(chars_s1) == len(chars_s2) and chars_s1 == chars_s2:
                return True
            
            right += 1
        
        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dict_s1 = {}

        for c in s1:
            dict_s1[c] = dict_s1.get(c, 0) + 1
        
        dict_s2 = {}
        left = 0
        right = 0

        while right < len(s1):
            dict_s2[s2[right]] = dict_s2.get(s2[right], 0) + 1
            right += 1
        
        while right < len(s2):
            if dict_s1 == dict_s2:
                return True
            
            dict_s2[s2[right]] = dict_s2.get(s2[right], 0) + 1
            right += 1
            dict_s2[s2[left]] -= 1
            if dict_s2[s2[left]] == 0:
                del dict_s2[s2[left]]
            left += 1
        
        return dict_s2 == dict_s1


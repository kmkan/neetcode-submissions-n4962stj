from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                key[idx] += 1
            key = tuple(key)
            res[key].append(s)

        return list(res.values()) 
    
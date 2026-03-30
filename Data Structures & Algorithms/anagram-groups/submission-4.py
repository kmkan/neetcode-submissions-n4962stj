class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                key[idx] += 1
            anagrams[tuple(key)].append(s)
        
        return list(anagrams.values())
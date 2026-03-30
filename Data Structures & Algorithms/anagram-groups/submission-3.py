class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            char_arr = [0] * 26
            for c in s:
                idx = ord('a') - ord(c)
                char_arr[idx] += 1
            key = tuple(char_arr)
            anagrams[key] = anagrams.get(key, [])
            anagrams[key].append(s)
        
        return list(anagrams.values())
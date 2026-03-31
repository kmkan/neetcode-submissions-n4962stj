class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = []


        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return ''.join(longest_prefix)
            longest_prefix.append(c)
        
        return ''.join(longest_prefix)
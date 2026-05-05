class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = []

        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return "".join(longest_prefix)
            longest_prefix.append(strs[0][i])
        
        return "".join(longest_prefix)
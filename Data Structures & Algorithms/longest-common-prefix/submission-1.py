class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = []

        base_word = strs[0]

        for i in range(len(base_word)):
            for word in strs:
                if i >= len(word) or word[i] != base_word[i]:
                    return "".join(longest_prefix)
            longest_prefix.append(base_word[i])
        
        return "".join(longest_prefix)
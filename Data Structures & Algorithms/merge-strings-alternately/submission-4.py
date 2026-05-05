class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pos = 0

        mergedStr = []
        while pos < len(word1) and pos < len(word2):
            mergedStr.append(word1[pos])
            mergedStr.append(word2[pos])
            pos += 1
        
        mergedStr.append(word1[pos:])
        mergedStr.append(word2[pos:])

        return ''.join(mergedStr)

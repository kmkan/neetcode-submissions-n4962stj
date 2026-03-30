class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = []

        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            merged_word.append(word1[i])
            merged_word.append(word2[j])
            i += 1
            j += 1
        
        merged_word.append(word1[i:])
        merged_word.append(word2[j:])
        
        return ''.join(merged_word)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}

        for i, c in enumerate(order):
            pos[c] = i
        
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]

            j = 0

            while j < len(first_word) and j < len(second_word) and first_word[j] == second_word[j]:
                j += 1
            
            if j < len(first_word) and j < len(second_word) and pos[first_word[j]] > pos[second_word[j]]:
                return False
            elif j >= len(second_word):
                return False


        return True
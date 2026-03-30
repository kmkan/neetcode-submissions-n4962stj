class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_chars = [0] * 26

        left = 0
        right = 0
        max_window = 0

        while right < len(s):
            freq_chars[ord(s[right]) - ord('A')] += 1
            max_char = max(freq_chars)
            while right - left + 1 - max_char > k:
                freq_chars[ord(s[left]) - ord('A')] -= 1
                left += 1
                max_char = max(freq_chars)
            
            max_window = max(max_window, right - left + 1)
            right += 1
        return max(max_window, right - left)
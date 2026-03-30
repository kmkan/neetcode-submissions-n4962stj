class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        left = 0
        right = 0
        max_size = 0
        while right < len(s):
            chars[ord(s[right]) - ord('A')] += 1
            max_char = max(chars)
            while right - left + 1 - max_char > k:
                chars[ord(s[left]) - ord('A')] -= 1
                max_char = max(chars)
                left += 1
            max_size = max(max_size, right - left + 1)
            right += 1
        
        return max_size

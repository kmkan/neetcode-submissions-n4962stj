class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        cur_chars = set()
        max_length = 0
        while right < len(s):
            if s[right] in cur_chars:
                cur_chars.remove(s[left])
                left += 1
            else:
                cur_chars.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
        
        return max_length
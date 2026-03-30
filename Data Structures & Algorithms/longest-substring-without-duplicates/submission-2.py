class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] in chars:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
            chars.add(s[right])
            right += 1
            longest = max(longest, len(chars))

        return longest
        
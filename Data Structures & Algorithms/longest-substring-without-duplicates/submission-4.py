class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        s_dict = {}

        for right in range(len(s)):
            char = s[right]
            if char in s_dict and s_dict[char] >= left:
                left = s_dict[char]+1
            s_dict[char] = right
            max_len = max(max_len, right-left+1)

        return max_len

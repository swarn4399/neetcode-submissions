class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_s = defaultdict(int)

        max_len = 0
        left = 0
        for right in range(len(s)):
            if s[right] in dict_s and dict_s[s[right]]>=left:
                left=dict_s[s[right]]+1
                dict_s[s[right]] = right
                curr_len = (right-left)+1
            else:
                dict_s[s[right]] = right
                curr_len = (right-left)+1
            max_len = max(max_len, curr_len)

        return max_len
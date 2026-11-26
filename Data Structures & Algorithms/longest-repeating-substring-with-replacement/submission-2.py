class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_str = {}
        longest = 0
        left = 0
        for right in range(len(s)):
            dict_str[s[right]] = 1+dict_str.get(s[right],0)
            most_freq = max(dict_str.values())
            if right-left-most_freq+1>k:
                dict_str[s[left]]-=1
                left+=1
            longest = max(longest, right-left+1)


        return longest
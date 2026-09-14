class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        dict_s = defaultdict(int)
        left = 0
        for right in range(len(s)):
            dict_s[s[right]]+=1
            max_freq = max(dict_s.values())
            while (right-left+1) - max_freq > k:
                dict_s[s[left]]-=1
                left+=1
                max_freq = max(dict_s.values())
            max_len = max(max_len, right-left+1)
        return max_len
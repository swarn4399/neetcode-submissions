class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_char = 0
        max_len = 0
        left = 0

        char_map = defaultdict(int)

        for i in range(len(s)):
            char = s[i]
            char_map[char]+=1

            max_char = max(max_char, char_map[char])

            while (i-left+1) - max_char > k:
                char_map[s[left]]-=1
                left+=1

            max_len = max(max_len, i-left+1)

        return max_len
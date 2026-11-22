class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        win_len = len(s1)
        left, right = 0, win_len
        curr_count = Counter(s2[left:right])
        while right<=len(s2):
            print(s2[left:right])
            curr_count = Counter(s2[left:right])
            if curr_count == s1_count:
                return True
                break
            else:
                left+=1
                right+=1
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for i in s:
            dict_s[i]+=1
        for j in t:
            dict_t[j]+=1
        if dict_s == dict_t:
            return True
        else:
            return False


        
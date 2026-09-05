class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s = defaultdict(list)
        res = []
        for s in strs:
            sort_s = "".join(sorted(s))
            dict_s[sort_s].append(s)

        res = []
        for item in dict_s:
            res.append(dict_s[item])

        return res
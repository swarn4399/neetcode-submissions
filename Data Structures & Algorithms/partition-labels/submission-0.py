class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_s = defaultdict(int)
        for i in range(len(s)):
            dict_s[s[i]] = i

        start, end = 0,0
        res=  []

        for j in range(len(s)):
            end = max(end, dict_s[s[j]])

            if j == end:
                res.append(end-start+1)
                start = end+1
        
        return res
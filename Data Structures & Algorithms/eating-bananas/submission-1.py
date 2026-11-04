class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kmin = 1
        kmax = max(piles)
        res = kmax

        while kmin<=kmax:
            kmid = (kmin+kmax)//2
            temp_h = sum((-(-pile//kmid)) for pile in piles)
            if temp_h<=h:
                kmax = kmid-1
                res = min(res,kmid)
            else:
                kmin = kmid+1
        return res
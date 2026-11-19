class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pos_set = {0,1,2}

        for trip in triplets:
            if trip[0]>target[0] or trip[1]>target[1] or trip[2]>target[2]:
                continue
            if trip[0]==target[0]:
                pos_set.discard(0)
            if trip[1]==target[1]:
                pos_set.discard(1)
            if trip[2]==target[2]:
                pos_set.discard(2)

        return False if pos_set else True
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_count = defaultdict(int)
        for n in hand:
            hand_count[n]+=1

        if len(hand)%groupSize:
            return False

        minH = list(hand_count.keys())
        heapq.heapify(minH)
        minH

        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i not in hand_count:
                    return False
                hand_count[i]-=1
                if hand_count[i]==0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
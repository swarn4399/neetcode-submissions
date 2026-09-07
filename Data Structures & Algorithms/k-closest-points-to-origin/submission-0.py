class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in points:
            distance = i[0]**2 + i[1]**2
            heapq.heappush(heap, (distance, i[0], i[1]))

        for j in range(k):
            temp = heapq.heappop(heap)
            res.append([temp[1], temp[2]])
        return res
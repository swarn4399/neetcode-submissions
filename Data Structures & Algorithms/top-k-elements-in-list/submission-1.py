class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = Counter(nums)

        res = []
        heap = []
        for num, count in dict_nums.items():
            heapq.heappush(heap, (count, num))

        while len(heap)>k:
            heapq.heappop(heap)

        for item in heap:
            res.append(item[1])

        return res
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pseudo_k = len(nums)-k
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for i in range(pseudo_k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
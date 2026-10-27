import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res=None
        for ele in nums:
            heapq.heappush(heap,(-ele)) #max heap
        for i in range(k):
            res = -1 * heapq.heappop(heap)
        return res

        
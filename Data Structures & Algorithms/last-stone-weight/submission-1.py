import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,i*(-1))
        while heap:
            val1 = -1 * heapq.heappop(heap)
            if heap:
                val2 = -1 *heapq.heappop(heap)
            else:
                return val1
            
            diff = val1-val2
            
            if diff:
                heapq.heappush(heap,diff*(-1))
            print(f"diff={diff}, val1={val1}, val2={val2}, heap={heap}")
        return 0

        
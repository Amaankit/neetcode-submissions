import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = []
        n = len(profits)
        for i in range(n):
            proj.append([capital[i],profits[i]])
        proj.sort()
        idx = 0
        heap=[]
        while(k>0):
            while(idx<n):
                if proj[idx][0] > w:
                    break
                else:
                    heapq.heappush(heap,proj[idx][1]*-1)
                    idx+=1
            if not heap:
                return w
            else:
                value = heapq.heappop(heap)
                w += (-1*value)
                k-=1
        return w

        
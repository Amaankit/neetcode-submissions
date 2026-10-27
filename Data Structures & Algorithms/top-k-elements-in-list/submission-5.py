import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        heap = []
        result = [] 
        counter = 0
        for ele in nums:
            hashmap[ele] = hashmap.get(ele,0) + 1
        for key,count in hashmap.items():
            if counter<k:
                heapq.heappush(heap,[count,key])
                counter+=1
                continue
            if heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap,[count,key])
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result



        
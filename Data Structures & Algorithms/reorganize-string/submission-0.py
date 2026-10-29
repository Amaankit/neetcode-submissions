import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        hashmap = {}
        heap = []
        seat = 0
        for ch in s:
            hashmap[ch] = 1+ hashmap.get(ch,0)
        for ch,freq in hashmap.items():
            heapq.heappush(heap,[(-1*freq),ch])

        while heap:
            pair1 =   heapq.heappop(heap)
            freq,ch =   pair1
            freq = -1*freq
            if(seat == 0 or res[seat-1]!= ch):
                res+=ch
                seat+=1
                freq-=1
                if freq > 0:
                    heapq.heappush(heap,[(-1*freq),ch])
            else:
                if not heap:
                    return ""
                pair2 =   heapq.heappop(heap)
                freq2,ch2 =   pair2
                freq2 = -1 * freq2
                if ch2 == ch:
                    return ""
                res+=ch2
                seat+=1
                freq2-=1
                if freq2 > 0:
                    heapq.heappush(heap,[-1*freq2,ch2])
                heapq.heappush(heap,[-1* freq,ch])

        return res
        
class Solution:


    def  totalEatingHours(self,piles: List[int], k: int):
        hour = 0
        for num in piles:
            hour += num//k
            if(num%k!=0):
                hour +=1
        return hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        min_hour = 0
        while(l<=r):
            mid = (l+r)//2
            
            hours = self.totalEatingHours(piles,mid)
            print(f"mid={mid}, l={l}, r={r}, hours={hours},h={h}")
            if hours> h:
                l=mid+1
            else:
                min_hour = mid
                r = mid -1
        return min_hour

        
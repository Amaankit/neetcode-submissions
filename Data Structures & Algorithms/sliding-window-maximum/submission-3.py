class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l=0
        r=0
        dq = collections.deque()

        while(r<len(nums)):
            
            # 2,3,4 case --> need to remove 3,2 
            while(dq and nums[dq[-1]]<nums[r]):
                dq.pop()

            dq.append(r)


            #moving window    
            if l> dq[0]:
                dq.popleft()
            
            if (r+1) >= k:
                result.append(nums[dq[0]])
                l+=1
            r+=1
        return result


            
            
        
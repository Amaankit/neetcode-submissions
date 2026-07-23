class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        prefix = [1 for i in range(length)]
        suffix = [1 for i in range(length)]
        for i in range(1,length):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(length-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(length):
            result.append(prefix[i]*suffix[i])
        return result



        
    
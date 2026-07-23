class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        prefix = [1 for i in range(length)]
        suffix = [1 for i in range(length)]
        for i in range(length):
            if i== 0:
                prefix[i]=1
            else:
                print(i,prefix[i-1],nums[i-1])
                prefix[i]=prefix[i-1]*nums[i-1]
        print(prefix)
        
        
        

        for i in range(length-1,-1,-1):
            print("i is ", i)
            if i== length-1:
                suffix[i]=1
            else:
                print(i,suffix[i+1],nums[i+1])
                suffix[i]=suffix[i+1]*nums[i+1]
                
        print(suffix)
        for i in range(length):
            result.append(prefix[i]*suffix[i])
        return result
        
        
        return result


        
    
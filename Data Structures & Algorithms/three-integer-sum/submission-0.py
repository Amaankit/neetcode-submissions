class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        length = len(nums)
        nums.sort()
        
        for i in range(length):

            if i >0 and nums[i] == nums[i-1]:
                continue


            left = i+1
            right = length -1 
            while(left < right):
                total = nums[i] + nums[left]+ nums[right]
                if(total==0):
                    results.append([nums[i] , nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif(total > 0):
                    right -=1
                else:
                    left+=1

        return results

        
class Solution:
    
    
    
    def __init__(self):
        self.ans = []
    
    #Optimal Approach

    def solve(self,nums,start_idx,remain,diary):
        if remain == 0:
            self.ans.append(diary.copy())

        for i in range(start_idx,len(nums)):
            if nums[i]> remain:
                break
            diary.append(nums[i])
            self.solve(nums,i,remain-nums[i],diary)
            diary.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.solve(nums,0,target,[])
        return self.ans




    #Normal Approach
    # def solve(self,nums,idx,target,total,diary):
        
    #     if idx == len(nums):
    #         if target == total:
    #             self.ans.append(diary.copy())
    #             return
    #         return
    #     if total> target:
    #         return
    #     ele = nums[idx]
    #     total +=ele
    #     diary.append(ele)
    #     self.solve(nums,idx,target,total,diary)
    #     total -=ele
    #     diary.pop()
    #     self.solve(nums,idx+1,target,total,diary)
    
        
    


    # def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     self.solve(nums,0,target,0,[])
    #     return self.ans
        
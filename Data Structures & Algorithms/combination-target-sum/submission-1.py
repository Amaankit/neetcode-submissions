class Solution:
    
    def __init__(self):
        self.ans = []
    def solve(self,nums,idx,target,total,diary):
        
        if idx == len(nums):
            if target == total:
                self.ans.append(diary.copy())
                return
            return
        if total> target:
            return
        ele = nums[idx]
        total +=ele
        diary.append(ele)
        self.solve(nums,idx,target,total,diary)
        total -=ele
        diary.pop()
        self.solve(nums,idx+1,target,total,diary)
    
        
    


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solve(nums,0,target,0,[])
        return self.ans
        
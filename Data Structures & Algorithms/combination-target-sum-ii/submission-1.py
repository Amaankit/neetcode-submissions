class Solution:
    
    def __init__(self):
        self.ans = []
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        def solve(candidates,start_idx,remain, diary):

            if remain == 0 :
                self.ans.append(diary.copy())
                return
            
            for i in range(start_idx,len(candidates)):

                if remain < candidates[i]:
                    break
                if i > start_idx and candidates[i-1]==candidates[i]:
                    continue
                diary.append(candidates[i])
                solve(candidates,i+1,remain-candidates[i], diary)
                diary.pop()
        solve(candidates,0,target,[])
        return self.ans
        

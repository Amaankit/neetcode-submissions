class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        candidates.sort()
        subarray = []
        result = []
        def help(start,target):
            if target == 0:
                result.append(subarray.copy())
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                subarray.append(candidates[i])
                help(i + 1, target - candidates[i])
                subarray.pop()
        help(0,target)
        return result
            
            


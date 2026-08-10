class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        sub_array = []
        def calculateSum(index,target):
            if target == 0:
                result.append(sub_array.copy())
                return
            if index >= len(nums) or target < 0:
                return
            if(nums[index]<=target):
                sub_array.append(nums[index])
                calculateSum(index,target-nums[index])
                sub_array.pop()
            calculateSum(index+1,target)

        calculateSum(0,target)
        return result
        
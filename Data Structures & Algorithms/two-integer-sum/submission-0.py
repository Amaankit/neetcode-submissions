class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0,len(nums)):
            if seen.get(target-nums[i]) != None:
                return [seen.get(target-nums[i]),i]
            else:
                seen[nums[i]] = i
        return []
        
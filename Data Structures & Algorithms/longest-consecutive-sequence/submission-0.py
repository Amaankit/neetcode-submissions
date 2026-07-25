class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=0
        num_set = set(nums)
        for n in nums:
            length = 0
            if n-1 not in num_set:
                while(n+length ) in num_set:
                    length +=1
                maximum=max(length,maximum)
        return maximum

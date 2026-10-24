class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        n = len(nums)
        right = n-1
        minimum= -1
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]> nums[n-1]):
                #part of part2 of array
                left = mid+1
            else:
                #part of part 1
                minimum = mid
                right = mid-1
        return nums[minimum]
        
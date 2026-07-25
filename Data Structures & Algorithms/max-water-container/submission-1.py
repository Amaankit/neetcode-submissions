class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0 
        right = len(heights)-1
        while(left<right):
            width = right - left #formula of width on x axis
            area = width * min(heights[left],heights[right])
            max_water = max(area,max_water)
            if heights[left] > heights[right]:
                right -=1
            else:
                left+=1
        return max_water




        
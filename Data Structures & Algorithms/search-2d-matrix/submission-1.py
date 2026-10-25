class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows*cols) -1
        while(low<=high):
            mid = (low + high)//2
            row = mid//cols
            col = mid%cols
            ele = matrix[row][col]
            if ele == target:
                return True
            elif ele > target:
                high = mid-1
            else:
                low = mid +1 
        return False

        
        
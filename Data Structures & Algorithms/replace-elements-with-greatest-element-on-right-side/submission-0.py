class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        len_arr=len(arr)
        rightMax = [0]*len_arr
        maxele=arr[::-1][0]
        for i in range(len_arr-1,-1,-1):
           rightMax[i]=maxele
           maxele= max(maxele,arr[i])
        rightMax[len_arr-1] = -1
        return rightMax


        
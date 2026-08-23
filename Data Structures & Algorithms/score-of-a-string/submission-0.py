class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(0,len(s)-1):
            result+= abs((ord(s[i+1]) - ord(s[i])))
        return result
        
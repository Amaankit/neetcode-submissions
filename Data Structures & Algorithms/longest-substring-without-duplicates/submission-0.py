class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_map={}
        left = 0 
        right = 0
        n = len(s)
        max_length = 0
        while(right<=n-1):
            while seen_map.get(s[right]) and left<right:
                #bee carefull, 
                print(s[right],left,right)
                #increaing left , thats why reducing left string frequency
                seen_map[s[left]]= seen_map[s[left]] - 1
                left+=1
            else:
                seen_map[s[right]]=1 + seen_map.get(s[right],0)
                max_length = max(max_length,right-left+1)
            right +=1
        return max_length


        
        
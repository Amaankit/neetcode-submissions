class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        freq = [0] * 26
        max_len = 0
        max_freq = 0
        while(r<len(s)):
            freq[ord(s[r])-ord('A')] = freq[ord(s[r])-ord('A')]+1
            max_freq = max(max_freq,freq[ord(s[r])-ord('A')])
            while((r-l+1) -max_freq > k):
                
                freq[ord(s[l])-ord('A')] = freq[ord(s[l])-ord('A')]-1
                max_freq = 0
                for f in freq:
                    max_freq = max(max_freq,f)
                l=l+1
            if((r-l+1) -max_freq <= k):
                max_len = max(max_len,r-l+1)
            r+=1
        return max_len
        
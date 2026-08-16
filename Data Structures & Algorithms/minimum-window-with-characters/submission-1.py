class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        win_map = {}
        #FOR DUPLICATE
        for i in t:
            win_map[i] = win_map.get(i, 0) + 1
        si=0
        count = 0
        min_len= 100000

        while (r < len(s)):

            if s[r] in win_map:
                if win_map[s[r]] > 0:
                    count += 1

                win_map[s[r]] -= 1
            
            

            
            while(count==len(t)):
                if min_len> r-l+1:
                    min_len = r-l+1
                    si = l
                if s[l] in win_map:
                    win_map[s[l]] += 1
                    # We have now lost a required character
                    if win_map[s[l]] > 0:
                        count -= 1
                l+=1
            r+=1
        if min_len == 100000:
            return ""
        return s[si:si+min_len]
        
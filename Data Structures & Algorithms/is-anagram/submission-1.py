class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        st = {}
        for i in range(len(s)):
            if st.get(s[i]):
                st[s[i]] +=1
            else:
                st[s[i]] = 1
            if st.get(t[i]):
                st[t[i]] -=1
            else:
                st[t[i]] = -1
        print(st)
        for i,j in st.items():
            if j!=0:
                return False
        return True
            
        
        
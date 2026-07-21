class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for st in strs:
            count = [0]*26
            for s in st:
                index = ord(s) - ord('a')
                count[index]+=1
            if result.get(str(count)):
                result[str(count)].append(st)
            else:
                result[str(count)] = [st]
        return list(result.values())
        
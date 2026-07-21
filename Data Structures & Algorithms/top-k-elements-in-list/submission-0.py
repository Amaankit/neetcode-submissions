class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        #Creating a hashmap
        for num in nums:
            if hashmap.get(num):
                hashmap[num]+=1
            else:
                hashmap[num]=1
        
        # Creating like on which index how much element exists , like if 3 ours 2 time then three will be on index 2
        result=[[] for _ in range(len(nums)+1)]
        for num,count in hashmap.items():
            print(count,num)
            result[count].append(num)
            print(result)
        
        # print(result)
        # print(hashmap)
        final_result = []
        for i in range(len(nums),0,-1):
            if result[i] != []:
                for j in result[i]:
                    final_result.append(j)
                    k-=1
                    if k==0:
                        return final_result
        return final_result


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        
        for i in strs:
            temp = [0]*26
            for j in i:
                ind = 97 - ord(j)
                temp[ind] +=1
            k = str(temp)
            if k in dic:
                dic[k].append(i)
            else:
                dic[k] = [i]
        print(dic)
        result = []
        for i in dic:
            result.append(dic[i])
        
        return result
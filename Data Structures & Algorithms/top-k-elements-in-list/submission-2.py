class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        length = max(dic.values())
        bucket = [[] for _ in range(length+1)]
        for i in dic:
            bucket[dic[i]].append(i)
        print(bucket)
        result = []
        while k>0:
            temp = bucket.pop()
            print(temp, type(temp))
            if temp:
                length = len(temp)
                k = k - length
                if k<0:
                    temp = temp[:k]
                for i in range(length):
                    result.append(temp[i])
        
        return result

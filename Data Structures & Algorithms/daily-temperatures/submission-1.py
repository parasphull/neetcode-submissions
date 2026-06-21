class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            count=0
            greater = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count +=1
                    greater=1
                    break
                count +=1
            if greater !=1:
                count = 0
            result[i] = count

        return result
            
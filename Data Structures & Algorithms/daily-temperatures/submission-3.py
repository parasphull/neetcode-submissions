class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            greater = 0
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    greater=1
                    count = j - i
                    break
            # if greater !=1:
            #     count = 0
            result[i] = count

        return result

            
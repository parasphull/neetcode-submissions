class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        i=len(temperatures) - 1
        while i>=0:
            if len(stack) == 0:
                result[i] = 0
                stack.append([temperatures[i],i])
            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                result[i] = stack[-1][1] - i if len(stack) > 0 else 0
                stack.append([temperatures[i], i])
            i-=1
        return result



            
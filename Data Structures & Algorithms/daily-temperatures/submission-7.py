class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        i=len(temperatures) - 1
        while i>0:
            if len(stack) == 0:
                stack.append([temperatures[i],i])
            else:
                if stack[len(stack)-1][0] < temperatures[i]:
                    stack[len(stack)-1][0] = temperatures[i]
                    stack[len(stack)-1][1] = i
                else:
                    stack.append([temperatures[i], i])
            i-=1
        print(stack)

        while len(stack) > 0:
            top = stack.pop()
            i=0
            while i < top[1]:
                if temperatures[i]<top[0] and result[i] == 0:
                    result[i] = top[1] - i
                i+=1
        return result



            
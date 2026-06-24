class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        soln_stack = []
        operators = ['+','-','*','/']
        for i in range(len(tokens)):
            if tokens[i] in operators:
                val1 = soln_stack.pop()
                val2 = soln_stack.pop()
                result = 0
                if tokens[i] == '+':
                    result = val1 + val2
                elif tokens[i] == '-':
                    result = val2 - val1
                elif tokens[i] == '*':
                    result = val1 * val2
                else:
                    result = int(val2 / val1)
                soln_stack.append(result)
            else:
                soln_stack.append(int(tokens[i]))
        
        return soln_stack[0]
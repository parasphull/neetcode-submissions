class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(','[','{']
        cp = [')',']','}']
        dic={'(':')','[':']','{':'}'}
        current_open = []
        # while len(arr)>0:
        i=0
        while i<len(s):
            if s[i] in op:
                current_open.append(s[i])
            else:
                if not current_open:
                    return False
                current = current_open.pop()
                if current == '' or dic[current] != s[i]:
                    return False
                    
            i+=1
        if len(current_open)>0:
            return False
        else:
            return True
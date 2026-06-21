class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        current_open = []
        i=0
        while i<len(s):
            if s[i] in dic.keys():
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
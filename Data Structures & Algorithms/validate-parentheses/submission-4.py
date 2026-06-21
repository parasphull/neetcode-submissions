class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        current_open = []
        for i in s:
            if i in dic:
                current_open.append(i)
            else:
                if not current_open:
                    return False
                current = current_open.pop()
                if dic[current] != i:
                    return False
        if len(current_open)>0:
            return False
        else:
            return True
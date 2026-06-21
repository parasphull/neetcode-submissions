class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] +=1
            else:
                dic[s[i]] = 1

            if t[i] in dic:
                dic[t[i]] +=1
            else:
                dic[t[i]] = 1
        
        for i in s:
            if i not in t:
                return False
            elif dic[i] % 2 != 0:
                return False
        
        return True


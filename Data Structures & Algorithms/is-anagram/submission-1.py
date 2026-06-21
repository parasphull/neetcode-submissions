class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dics = {}
        dict = {}
        for i in range(len(s)):
            if s[i] in dics:
                dics[s[i]] +=1
            else:
                dics[s[i]] = 1

            if t[i] in dict:
                dict[t[i]] +=1
            else:
                dict[t[i]] = 1

        print(dics)
        print(dict)
        
        for i in dics:
            if i not in dict:
                print("not in", i)
                return False
            elif (dics[i] + dict[i]) % 2 != 0:
                return False
        
        return True


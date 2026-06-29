class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        is_per = True
        s1_dic = {}
        if len(s2) < len(s1):
            return False
        for i in s1:
            if i in s1_dic:
                s1_dic[i] += 1
            else:
                s1_dic[i] = 1
        for i in range(len(s2)-(k-1)):
            sub_str = s2[i:i+k]
            sub_dic={}
            is_per = True
            for j in sub_str:
                if j in sub_dic:
                    sub_dic[j] += 1
                else:
                    sub_dic[j] = 1

            for j in sub_dic:
                if j in s1_dic:
                    if sub_dic[j] != s1_dic[j]:
                        is_per = False
                else:
                    is_per = False
            if is_per:
                break
        
        return is_per
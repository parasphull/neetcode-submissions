class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        s1_arr = [0]*26
        for i in s1:
            ind = ord(i) - 97
            s1_arr[ind] +=1
        
        s1_key = str(s1_arr)
        lt_ptr = 0
        rt_ptr = k
        substr = s2[:k]
        s2_arr=[0]*26
        for j in substr:
            ind = ord(j) - 97
            s2_arr[ind] +=1
        s2_key = str(s2_arr)
        if s1_key == s2_key:
            return True

        while rt_ptr<len(s2):
            lt_ind = ord(s2[lt_ptr]) - 97
            s2_arr[lt_ind] -=1
            lt_ptr+=1

            rt_ind = ord(s2[rt_ptr]) - 97
            s2_arr[rt_ind] +=1
            rt_ptr+=1

            s2_key = str(s2_arr)
            if s1_key == s2_key:
                return True

        # for i in range (len(s2)-(k-1)):
        #     substr = s2[i:i+k]
        #     s2_arr=[0]*26
        #     for j in substr:
        #         ind = ord(j) - 97
        #         s2_arr[ind] +=1
            
        #     s2_key = str(s2_arr)
        #     if s1_key == s2_key:
        #         return True
        
        return False


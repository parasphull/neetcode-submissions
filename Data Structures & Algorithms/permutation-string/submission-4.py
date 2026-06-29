class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        s1_arr = [0]*26
        for i in s1:
            ind = ord(i) - 97
            s1_arr[ind] +=1
        
        s1_key = str(s1_arr)
        
        for i in range (len(s2)-(k-1)):
            substr = s2[i:i+k]
            s2_arr=[0]*26
            for j in substr:
                ind = ord(j) - 97
                s2_arr[ind] +=1
            
            s2_key = str(s2_arr)
            print(s1_key, s2_key)
            if s1_key == s2_key:
                return True
        
        return False


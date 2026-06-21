class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            encoded_str = encoded_str + str(len(i)) + '#' + i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        temp = ''
        i=0
        end = 0
        while(i<len(s)):
            if s[i] == '#':
                length = int(s[end:i])
                end = i+1+length
                temp = s[i+1:end]
                result.append(temp)
                i=end
            else:
                i+=1


        
        return result 
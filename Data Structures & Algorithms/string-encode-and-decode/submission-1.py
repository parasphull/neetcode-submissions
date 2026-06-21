class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            encoded_str = encoded_str + i + '-'
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        temp = ''
        for i in s:
            if i == '-':
                result.append(temp)
                temp = ''
            else:
                temp = temp + i
            

        return result 
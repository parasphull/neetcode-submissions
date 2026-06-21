class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ''
        for i in s:
            if i.isalnum():
                string = string + i.lower()
        
        reversed_str = string[::-1]

        return string == reversed_str
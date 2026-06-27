class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt_ptr=0
        rt_ptr=0
        max_len=0
        substr = ''
        while lt_ptr<=rt_ptr and rt_ptr<len(s):
            if len(substr)<1:
                substr = substr + s[lt_ptr]
            if lt_ptr == rt_ptr and rt_ptr != len(s)-1:
                rt_ptr+=1
            if s[rt_ptr] not in substr:
                substr += s[rt_ptr]
                rt_ptr +=1
            else:
                max_len = max(max_len, len(substr))
                lt_ptr+=1
                rt_ptr = lt_ptr+1
                substr=''
        if substr !='':
            max_len = max(max_len, len(substr))

        return max_len
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt_ptr=0
        rt_ptr=0
        max_len=0
        while lt_ptr<=rt_ptr and rt_ptr<len(s):
            if lt_ptr == rt_ptr and rt_ptr != len(s)-1:
                rt_ptr+=1
            if s[rt_ptr] not in s[lt_ptr:rt_ptr]:
                rt_ptr +=1
            else:
                max_len = max(max_len, rt_ptr-lt_ptr)
                lt_ptr+=1
        max_len = max(max_len, rt_ptr-lt_ptr)

        return max_len
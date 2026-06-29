class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt_ptr=0
        rt_ptr=0
        max_len=0
        count_dic = {}
        while lt_ptr<=rt_ptr and rt_ptr<len(s):
            if s[rt_ptr] in count_dic and count_dic[s[rt_ptr]] == 1:
                max_len = max(max_len, (rt_ptr-lt_ptr))
                if s[rt_ptr] == s[lt_ptr]:
                    count_dic[s[rt_ptr]] = 0
                count_dic[s[lt_ptr]] = 0
                lt_ptr+=1
            else:
                count_dic[s[rt_ptr]] = 1
                rt_ptr+=1
            
        max_len = max(max_len, (rt_ptr-lt_ptr))

        return max_len
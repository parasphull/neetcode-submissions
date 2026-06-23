class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1=0
        p2=len(heights)-1
        max_vol = 0
        while p2>p1:
            l = min(heights[p1], heights[p2])
            b = p2-p1
            vol= l*b
            if vol > max_vol:
                max_vol = vol
            
            if heights[p1] <= heights[p2]:
                p1+=1
            else:
                p2-=1
        
        return max_vol
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                b = j-i
                l= min(heights[i], heights[j])
                volume = l*b
                if volume > max_volume:
                    max_volume = volume
            
        return max_volume
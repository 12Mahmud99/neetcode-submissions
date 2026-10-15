class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        m=0
        while i < j:
            a=min(heights[i],heights[j])*(j-i)
            if a>=m:
                m=a
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return m
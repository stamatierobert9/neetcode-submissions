class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] <= heights[r]:
                area = (r - l) * heights[l]
                if max < area:
                    max = area
                l += 1
            elif heights[l] >= heights[r]:
                area = (r - l) * heights[r]
                if max < area:
                    max = area
                r -= 1
        
        return max
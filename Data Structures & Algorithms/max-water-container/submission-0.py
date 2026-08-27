class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = -float('inf')

        while l < r:
            left, right = heights[l], heights[r]
            

            if left < right:
                area = left * (r - l)
                l += 1
            else:
                area = right * (r - l)
                r -= 1

            best = max(best, area)

        return best
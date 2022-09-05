class Solution:
    def maxArea(self, height: List[int]) -> int:
        first=0
        maxArea=0
        second=len(height)-1
        while first<second:
            length=second-first
            h=min(height[second],height[first])
            maxArea=max(maxArea,length*h)
            if height[second]>height[first]:
                first+=1
            else:
                second-=1
        return maxArea
        
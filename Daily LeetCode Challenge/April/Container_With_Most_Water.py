# LeetCode 11. 

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""

class Solution(object):
    def maxArea(self, height):
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            min_height=min(height[l], height[r])
            area = max(area, (r - l) * min_height)
            if height[l] < height[r]:
                l+=1
                while height[l]<min_height:
                    l+=1
            else:
                r-=1
                while height[r]<min_height:
                    r-=1			
        return area

# LeetCode 1046. 

"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
"""

from sortedcontainers import SortedList

class Solution(object):
    def lastStoneWeight(self, stones):
        sl = SortedList(stones)
        while len(sl) >= 2:
            y = sl.pop()
            x = sl.pop()
            if y > x: sl.add(y - x)  # Note that sl is a SortedList
        return sl.pop() if len(sl) else 0
			

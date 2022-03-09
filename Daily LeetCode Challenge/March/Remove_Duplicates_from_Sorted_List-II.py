# LeetCode 82. 

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.


Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = {}
        h = ret = ListNode(0)
        while head:
            if head.val not in l.keys():
                l[head.val] = 1
            else:
                l[head.val] += 1
            head = head.next
        for i in l.keys():
            if l[i] == 1:
                # print(i)
                ret.next = ListNode(i)
                ret = ret.next
        return h.next
			

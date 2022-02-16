# LeetCode 24

'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head
 
    prev, cur, ans = None, head, head.next
   
    while cur and cur.next:
        adj = cur.next
        if prev: prev.next = adj
        cur.next, adj.next = adj.next, cur
        prev, cur = cur, cur.next
         
    return ans or head
  

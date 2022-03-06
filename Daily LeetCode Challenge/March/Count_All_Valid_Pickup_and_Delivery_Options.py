# LeetCode 1359. 

"""
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1

Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
"""

def countOrders(self, n: int) -> int:
    if n == 1:
        return 1
    else:
        return (n*(2*n-1)*self.countOrders(n-1))%(10**9+7)
      

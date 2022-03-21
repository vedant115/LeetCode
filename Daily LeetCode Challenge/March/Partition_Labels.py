# LeetCode 763. 

"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""

def partitionLabels(self, s: str) -> List[int]:
    arr = [s[0]]
    ans = [0]
    
    for i in range(len(s)):
        # check new ele
        if (s[i] not in arr):
            # check if elements of arr present further in string
            for j in range(len(arr)):
                if arr[j] in s[i+1:]:
                    arr.append(s[i])
                    break
                # no ele of arr in further string 
                # append len of resultant string and initialize arr with new ele
                if j == len(arr)-1:
                    ans.append(i-sum(ans))
                    arr = [s[i]]
    
    ans.append(i-sum(ans)+1)
    return (ans[1:])
	

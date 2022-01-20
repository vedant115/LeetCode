class Solution:
    def divideString(self, s, k, fill):
        ans=[]
        for i in range(0,len(s),k):
            temp=s[i:i+k]
            temp=temp.ljust(k, fill)
            ans.append(temp)
        return ans

# LeetCode 127

'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
'''

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList=set(wordList)
    if endWord not in wordList:
        return 0
    que=[beginWord]
    j=0
    while que:
        j=j+1
        l=len(que)
        while l:
            curr=que[0]
            del que[0]
            for i in range(len(curr)):
                for k in range(ord("a"),ord("z")+1):
                    new_word=curr[:i]+chr(k)+curr[i+1:]
                    if new_word==endWord:
                        return j+1
                    if new_word in wordList:
                        que.append(new_word)
                        wordList.remove(new_word)
            l=l-1
    return 0
  

#Leetcode question Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Time: O(n2)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        subsDict={}
        max_len=0
        j=0
        if (len(s)>0 and not s.isspace()):
            while(j<len(s)):
                for i in s[j:]:
                    if i in subsDict:
                        current_len = len(subsDict)
                        subsDict={}
                        if current_len > max_len:
                            max_len = current_len
                        j=j+1
                        break
                    else:
                        subsDict[i]=1
        elif s.isspace():
            return 1
        else:
            return 0
        return max_len
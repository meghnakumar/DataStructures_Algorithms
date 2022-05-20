#Leetcode question link: https://leetcode.com/problems/valid-anagram/
#Time complexity = O(n)

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dict={}
        dict2={}
        for i in s:
            if i in dict:
                dict[i]= dict[i]+1
            else:
                dict[i]=1
        for i in t:
            if i in dict2:
                dict2[i]=dict2[i]+1
            else:
                dict2[i]=1
        for i in dict:
            if i in dict2:
                if dict[i]==dict2[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True
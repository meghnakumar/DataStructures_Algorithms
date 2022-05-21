#Leetcode question link: https://leetcode.com/problems/valid-parentheses/

#It is a classic stack problem.

class Solution(object):
    def isValid(self, s):
        parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if parentheses.get(char):
                if not stack:
                    return False
                else:
                    if stack[-1] == parentheses[char]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        return not stack
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occ = {}

        stack=[]
        visited = set()

        for i in range(len(s)):
                last_occ[s[i]] = i

        for i in range(len(s)):

                if s[i] not in visited:
                    while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                        visited.remove(stack.pop())

                    stack.append(s[i])
                    visited.add(s[i])

        return ''.join(stack)
#         dict={}
#         stack=[]
#         for i in range(len(s)):
#             dict[i] = s[i]
#         print dict
#         for l in s:
#             if len(stack)>0:
#                 if stack[-1]<l:
#                     stack.append(l)
#                 elif stack[-1]>l:
#                     if stack[-1]
                    
#             else:
#                 stack.append(l)
#         return stack
#         for ch in dict:
#             stack.append(ch)
        
#         return ''.join(sorted(stack))
#         letter = [l for l in s]
#         stack = {}
        
#         print letter
#         i=0
#         for l in letter:
#             if len(stack)>0:
#                 print l
#                 if l not in stack:
#                     stack[i]=l
#                     i=i+1
#             else:
#                 stack[0]=l
#         return stack
        
    
        
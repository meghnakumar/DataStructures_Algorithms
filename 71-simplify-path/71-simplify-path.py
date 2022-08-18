class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
#         stack=[]
#         m=0
#         s=''
#         for i in path:
#             if m==0:
#                 if i=='/':
#                     stack.append(i)
#                 else:
#                     return s
#                 m=m+1
#             else:
#                 if i=='.':
#                     if stack[-1]=='.':
                        
#                     stack=stack;
#                 elif i=='/':
#                     if stack[-1]=='/':
#                         stack=stack;
#                     else:
#                         stack.append(i)
#                 else:
#                     stack.append(i)
#             print stack
#         if len(stack)>1 and stack[-1]=='/':
#             stack.pop()
#         for i in stack:
#             s=s+i
#         return s

        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
                
            
            
            
            
        
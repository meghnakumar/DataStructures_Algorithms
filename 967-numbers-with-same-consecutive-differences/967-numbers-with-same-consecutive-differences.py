class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = range(1, 10)
        for i in range(n - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + k, x % 10 - k] if 0 <= y <= 9}
        return list(cur)
#         arr=[]
#         for i in range(0,9):
#             str1=''
#             s=n
#             while s!=0:
#                 if (i+k) in range(0,9):
#                     if str1=='' and (i+k)==0:
#                         continue
#                     else:
#                         str1=str1+str(i)
#                     s=s-1
                    
#             arr.append(int(str1))
            
#         return arr
                    
        
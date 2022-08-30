class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
#         index=0
#         print(len(nums))
#         while index<len(nums)-1:
#             # if index==0:
#             #     if nums[index]==0:
#             #         break
#             #     index=index+1
#             # else:
#             if nums[index]==0:
#                 break
#             index=max(index+nums[index], index)
#         print(index)
#         if index==len(nums)-1:
#             return True
#         return False
            
    
            
        